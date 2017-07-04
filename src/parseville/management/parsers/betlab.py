# -*- coding: utf-8 -*-
import re
import urllib, json

from dateutil import parser
from helper import get_soup_from_url
from parseville.models import Company, Vacancy, Country, City, Event, Office, News


def parse_vacancy(save):
    company = Company.objects.get(alias='betlab')
    url = 'https://jobs.dou.ua/companies/betlab/vacancies/export/'
    response = urllib.urlopen(url)
    vacancies = json.loads(response.read())
    for vacancy in vacancies:
        print vacancy['title']
        name = vacancy['title']
        description = vacancy['description'].encode('utf-8')
        short_text = vacancy['category']
        url = vacancy['link']
        date = vacancy['published']
        vacancy_obj, created = Vacancy.objects.get_or_create(name=name, company=company)
        vacancy_obj.alias = re.sub(" ", "-", name.lower())
        vacancy_obj.description = description
        vacancy_obj.url = url
        vacancy_obj.extra = short_text
        vacancy_obj.date = date
        vacancy_obj.save()
