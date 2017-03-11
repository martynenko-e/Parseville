# -*- coding: utf-8 -*-
import re
import time
from helper import get_soup_from_url, download_image
from parseville.models import Company


def parse_company(save):
    soup = get_soup_from_url('https://jobs.dou.ua/ratings/%D0%9A%D0%B8%D0%B5%D0%B2/', save)
    if soup:
        company_elements = soup.findAll('td', class_="company-name")
        if company_elements:
            for company in company_elements:
                time.sleep(1)
                company_url = company.a['href'][:-5]
                soup = get_soup_from_url(company_url, save)
                if soup:
                    company_name = soup.find('div', class_="g-company-wrapper")
                    if company_name:
                        company_name = company_name.h1.text.strip()
                    company_logo = soup.find('div', class_="g-company-wrapper")
                    if company_logo.img:
                        company_logo = company_logo.img['src']
                    company_offices = soup.find('div', class_="offices")

                    if company_offices:
                        company_offices = company_offices.text.strip()
                    company_site = soup.find('div', class_="site")
                    if company_site:
                        company_site = company_site.a['href']
                    company_description = soup.find('div', class_="b-company-about").find('div', class_="b-typo")
                    if company_description:
                        company_description = company_description.div
                    company_obj, created = Company.objects.get_or_create(name=company_name)
                    if created:
                        print "company added: %s" % company_name
                        company_obj.alias = re.sub("-", " ", company_name.lower())
                        try:
                            company_obj.description = company_description.encode('utf-8')
                        except Exception as e:
                            print "description is fail for company: %s" % company_name
                        company_obj.url = company_site
                        company_obj.extra = company_offices
                        company_obj.save()
                        download_image(company_obj, company_logo)