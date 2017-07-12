# -*- coding: utf-8 -*-
import re
import urllib, json

from dateutil import parser
from helper import get_soup_from_url
from parseville.models import Company, Vacancy, Country, City, Event, Office, News


def parse_vacancy(save):
    company = Company.objects.get(alias='grammarly')
    url = 'https://api.greenhouse.io/v1/boards/grammarly/embed/departments?callback='
    response = urllib.urlopen(url)
    file_with_data = json.loads(response.read())
    departments = file_with_data['departments']
    engineering_department = departments[0]
    engineering_department_jobs = engineering_department['jobs']
    for job in engineering_department_jobs:
        vacancy_title = job['title']
        print vacancy_title
        vacancy_city = job['location']['name']
        vacancy_link = job['absolute_url']
        soup = get_soup_from_url(vacancy_link, save)
        if soup:
            content = soup.findAll('p')
            list_of_qualifications = soup.findAll('ul')
            description = content
            vacancy_obj, created = Vacancy.objects.get_or_create(name=vacancy_title, company=company)
            vacancy_obj.alias = re.sub(" ", "-", vacancy_title.lower())
            vacancy_obj.description = description
            vacancy_obj.extra = list_of_qualifications
            vacancy_obj.url = vacancy_link
            vacancy_obj.save()
