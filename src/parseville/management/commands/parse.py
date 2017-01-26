# -*- coding: utf-8 -*-
import re
import urllib2
import time

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from PIL import Image
from StringIO import StringIO

from django.utils.text import slugify

from parseville.models import Company


class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
        if len(args) == 0:
            test(False)
        else:
            test(True)


def test(save):
        soup = get_soup_from_url('https://jobs.dou.ua/ratings/%D0%9A%D0%B8%D0%B5%D0%B2/', save)
        if soup:
            company_elements = soup.findAll('td', class_="company-name")
            if company_elements:
                for company in company_elements:
                    time.sleep(1)
                    company_url = company.a['href'][:-5]
                    soup = get_soup_from_url(company_url, save)
                    if soup:
                        company_name = soup.find('div', class_="g-company-wrapper").h1.text.strip()
                        company_logo = soup.find('div', class_="g-company-wrapper").img['src']
                        company_offices = soup.find('div', class_="offices")
                        if company_offices:
                            company_offices = company_offices.text.strip()
                        compamy_site = soup.find('div', class_="site").a['href']
                        company_description = soup.find('div', class_="b-company-about").find('div', class_="b-typo").div
                        company_obj, created = Company.objects.get_or_create(name=company_name)
                        if created:
                            print "company added: %s" % company_name
                            company_obj.alias = re.sub("-", " ", company_name.lower())
                            try:
                                company_obj.description = company_description.encode('utf-8')
                            except Exception as e:
                                print "description is fail for company: %s" % company_name
                            company_obj.site_url = compamy_site
                            company_obj.country = "Ukraine"
                            company_obj.office = company_offices
                            company_obj.save()
                            download_image(company_obj, company_logo)


def get_soup_from_url(url, save):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

    r = requests.get(url, headers=headers, timeout=30)

    # make sure that the page exist

    if r.status_code == 200:
        html = r.text
        if save:
            file1 = open("parse.html", "w")
            file1.write(html.encode('utf-8'))
            file1.close()
        return BeautifulSoup(html, 'lxml')

    else:
        print "Can't read url %s, status code %s" % (url, r.status_code)


def download_image(self, url):
    input_file = StringIO(urllib2.urlopen(url).read())
    output_file = StringIO()
    img = Image.open(input_file)
    # if img.mode != "RGB":
    #     img = img.convert("RGB")
    img.save(output_file, "PNG")
    try:
        self.logo.save(slugify(self.name).lower() + ".png", ContentFile(output_file.getvalue()),
                       save=True)
    except Exception as e:
        self.logo.save(self.name.lower() + ".png", ContentFile(output_file.getvalue()), save=True)