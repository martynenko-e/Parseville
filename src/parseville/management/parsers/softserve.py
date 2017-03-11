# -*- coding: utf-8 -*-
import re
from helper import get_soup_from_url, download_image
from parseville.models import Company, Vacancy


def parse_vacancy(save):
    soup = get_soup_from_url(
        'https://softserve.ua/en/vacancies/open-vacancies/?tax-direction=0&tax-country=117&tax-city=121', save)
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
                        vacancy_obj.url = vacancy_url
                        vacancy_obj.extra = city + " languages " + lang
                        vacancy_obj.save()