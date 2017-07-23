# -*- coding: utf-8 -*-
import re
import urllib, json

# from dateutil import parser
from helper import get_soup_from_url
from parseville.models import (
    Company,
    Vacancy,
    Country, 
    City, 
    Event, 
    Office, 
    News
    )


def parse_vacancy(save):
    company = Company.objects.get(alias='ciklum')
    soup = get_soup_from_url('https://jobs.ciklum.com/search-and-apply/', save)
    basic_list = soup.ol
    vacancy_list = basic_list.find_all('div', class_='position-name')
    for vacancy_item in vacancy_list:
        vacancy_link = vacancy_item.find('a').get('href')
        vacancy_title = vacancy_item.find('a').text.encode('utf-8')
        vacancy_soup = get_soup_from_url(vacancy_link, save)
        if vacancy_soup:
            vacancy_header = vacancy_soup.find('div', id='job-detail') \
                .find('div', class_='details-text') \
                .find('div', class_='section_header')
            vacancy_city = vacancy_header.find('h2').find('strong').text.encode('utf-8')
            vacancy_body = vacancy_soup.find('div', id='job-detail') \
                .find('div', class_='details-text') \
                .find('div', class_='section_content')
            # plain text in html how to parse ?
            vacancy_desc = vacancy_body.find('p').text
            vacancy_date = parser.parse(vacancy_body.find('p', class_='section-name').text[8:])
            print vacancy_title
            vacancy_obj, created = Vacancy.objects.get_or_create(name=vacancy_title, company=company)
            vacancy_obj.alias = re.sub(" ", "-", vacancy_title.lower())
            vacancy_obj.description = vacancy_desc
            vacancy_obj.url = vacancy_link
            vacancy_obj.extra = vacancy_city
            vacancy_obj.date = vacancy_date
            vacancy_obj.save()
