# -*- coding: utf-8 -*-
import re
from helper import get_soup_from_url
from parseville.models import Company, Vacancy, Country, City, Office


def parse_vacancy(save):
    soup = get_soup_from_url('http://cogniance.com/careers/', save)
    if soup:
        vacancy_elements = soup.find('div', class_='careers-list'). \
            find('ul', class_='locations-position').findAll('li', class_='careers-item col')
        if vacancy_elements:
            for vacancy in vacancy_elements:
                vacancy_url = vacancy.a['href']
                vacancy_title = vacancy.strong.text
                soup = get_soup_from_url(vacancy_url, False)
                if soup:
                    desc = soup.find('div', class_='col-profile-left col')
                    card = soup.find('h1', class_='modal-title')
                    if card:
                        title = card.find('strong', id='job-position').text
                        city = card.find('div', id='job-location').text
                        lang = ''
                        print title, city, lang
                        comp = Company.objects.get(alias='cogniance')

                        vacancy_obj, created = Vacancy.objects.get_or_create(name=title, company=comp)
                        vacancy_obj.alias = re.sub(' ', '-', title.lower())
                        vacancy_obj.description = desc.encode('utf-8')
                        vacancy_obj.url = vacancy_url
                        vacancy_obj.extra = city + ' languages ' + lang
                        vacancy_obj.save()
