# -*- coding: utf-8 -*-
import re
from helper import get_soup_from_url, download_image
from parseville.models import Company, Vacancy, Country, City, Office


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


def parse_offices(save):
    company = Company.objects.get(alias="softserve")
    soup = get_soup_from_url(
        'https://softserve.ua/en/contacts/', save)
    if soup:
        group_contact = soup.find("div", class_='panel-group-contact')
        country_list = group_contact.findAll("h4", class_="panel-title")
        panel_collapse = group_contact.findAll("div", class_="panel-collapse collapse")
        for panel_index, panel in enumerate(panel_collapse):
            office_country = country_list[panel_index].text.strip()
            country_obj, created = Country.objects.get_or_create(name=office_country)
            scripts = panel.findAll("script")
            media_contacts = panel.findAll("div", class_="media media-contact js-linkAccordion")
            for index, media in enumerate(media_contacts):

                lat = re.findall(r'lat:.*,', scripts[index].text.strip())[0][4:-1]
                lng = re.findall(r'lng:.*,', scripts[index].text.strip())[0][4:-1]
                office_city = media.find("h2", class_="media-contact_name").text.strip()
                office_name = media.find("div", class_="media-contact_describe").text.strip()
                office_address = media.find("div", class_="media-contact_connect").findAll("p")[0].text.strip()
                office_tel = media.find("div", class_="media-contact_connect").findAll("p")[1].text.strip()
                office_fax = media.find("div", class_="media-contact_connect").findAll("p")[2].text.strip()
                office_email = media.find("div", class_="media-contact_connect").findAll("a")[0].text.strip()
                city_obj, created = City.objects.get_or_create(name=office_city, country=country_obj)
                Office.objects.get_or_create(name=office_name,
                                             city=city_obj,
                                             company=company,
                                             latitude=lat,
                                             longitude=lng,
                                             address=office_address,
                                             phone=' '.join(office_tel.split()),
                                             email=office_email)
