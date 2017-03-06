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

from parseville.models import Vacancy, Company, ProgrammingLanguage, City


class Command(BaseCommand):
    args = '<save>'
    can_import_settings = True

    def handle(self, *args, **options):
        if len(args) is 1 and args[0] == 'save':
            test(True)
        if len(args) == 0:
            test(True)


def test(save):
        soup = get_soup_from_url('https://softserve.ua/ua/vacancies/open-vacancies/?tax-direction=0&tax-country=117&tax-city=121', save)
        if soup:
            vacancy_elements = soup.find('div', class_="col-xs-12 col-md-8").findAll('div', class_="col-xs-12")
            if vacancy_elements:
                for vacancy in vacancy_elements:
                    vacancy_url = vacancy.a['href']
                    vacancy_title = vacancy.h3.text
                    soup = get_soup_from_url(vacancy_url, False)
                    if soup:
                        desc = soup.find('div', class_='content-vacancy')
                        card = soup.find('div', class_='card-vacancy-prev')
                        if card:
                            title = card.find('h2', class_='card-vacancy-prev_title').text
                            dd = card.findAll('dd')
                            city = ""
                            lang = ""
                            if dd:
                                lang = dd[0].text
                                country = dd[1].text
                                city = dd[2].text
                            # print desc
                                print title, lang, country, city
                            comp = Company.objects.get(alias="softserve")

                            vacancy_obj, created = Vacancy.objects.get_or_create(name=title, company=comp)
                            vacancy_obj.alias = re.sub(" ", "-", title.lower())
                            vacancy_obj.description = desc.encode("utf-8")
                            vacancy_obj.vacancy_url = vacancy_url
                            vacancy_obj.extra = city + " languages " + lang
                            vacancy_obj.save()

                    # name = models.CharField(max_length=200)
                    # alias = models.CharField(max_length=200)
                    # description = models.TextField(blank=True, null=True)
                    # date_of_publication = models.DateField(blank=True, null=True)
                    # show = models.BooleanField(default=False)
                    # show_on_main = models.BooleanField(default=False)
                    # vacancy_url = models.URLField(null=True, blank=True)
                    # company = models.ForeignKey(Company)
                    # city = models.ForeignKey(City)
                    # programming_language = models.ForeignKey(ProgrammingLanguage, null=True, blank=True)


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