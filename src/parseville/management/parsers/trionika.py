# -*- coding: utf-8 -*-
import re
from helper import get_soup_from_url
from parseville.models import Company, Vacancy, Country, City, Office


def parse_vacancy(save):
    soup = get_soup_from_url('http://trionika.com/', save)
    if soup:
        vacancy_elements = soup.findAll('div', class_='benefits-header-list')
        if vacancy_elements:
            for vacancy in vacancy_elements:
                vacancy_url = '#'
                vacancy_title = vacancy.findAll('div', class_='wow fadeInUp')
                for title in vacancy_title:
                    desc = 'trionika style lol'
                    print title.text
                    comp = Company.objects.get(alias='trionika')
                    print comp.name
                    vacancy_obj, created = Vacancy.objects.get_or_create(name=title.text, company=comp)
                    vacancy_obj.alias = re.sub(' ', "-", title.text.lower())
                    vacancy_obj.description = desc
                    vacancy_obj.url = vacancy_url
                    vacancy_obj.extra = ' '
                    vacancy_obj.save()
