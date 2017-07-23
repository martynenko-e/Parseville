# -*- coding: utf-8 -*-
import re
from helper import get_soup_from_url
from parseville.models import (
    Company,
    Vacancy, 
    Country, 
    City, 
    Office, 
    Event
    )


def parse_vacancy(save):
    company = Company.objects.get(alias='cogniance')
    soup = get_soup_from_url('http://cogniance.com/careers/', save)
    if soup:
        vacancy_elements = soup.find('div', class_='careers-list'). \
            find('ul', class_='locations-position').findAll('li', class_='careers-item col')
        if vacancy_elements:
            for vacancy in vacancy_elements:
                vacancy_url = vacancy.a['href']
                # vacancy_title = vacancy.strong.text
                soup = get_soup_from_url(vacancy_url, False)
                if soup:
                    desc = soup.find('div', class_='col-profile-left col')
                    card = soup.find('h1', class_='modal-title')
                    if card:
                        title = card.find('strong', id='job-position').text
                        city = card.find('div', id='job-location').text
                        print title, city
                        vacancy_obj, created = Vacancy.objects.get_or_create(name=title, company=company)
                        vacancy_obj.alias = re.sub(" ", "-", title.lower())
                        vacancy_obj.description = desc.encode("utf-8")
                        vacancy_obj.url = vacancy_url
                        vacancy_obj.extra = city
                        vacancy_obj.save()


def parse_offices(save):
    company = Company.objects.get(alias='cogniance')
    soup = get_soup_from_url('http://cogniance.com/get-in-touch/', save)
    if soup:
        office_list_kyiv = soup.find('div', class_='popover-list').find('div', id='kyiv')
        print office_list_kyiv
        if office_list_kyiv:
            office = office_list_kyiv.find('address')
            if office:
                office_city = office.find('h3').find('strong').text.encode('utf-8')
                city = City.objects.get(name='Kyiv')
                office_address = office.findAll('h4')[0].text
                office_email = office.findAll('h4')[3].find('a', class_='external').text
                Office.objects.get_or_create(name=office_city,
                                             city=city,
                                             company=company,
                                             latitude=2,
                                             longitude=3,
                                             address=office_address,
                                             phone=03,
                                             email=office_email
                                             )


def parse_events(save):
    company = Company.objects.get(alias='cogniance')
    soup = get_soup_from_url('http://cogniance.com/insights/', save)
    if soup:
        events_list = soup.find('div', class_='all-events').findAll('div', class_='event')
        if events_list:
            for event in events_list:
                # todo  -> date formatting
                event_date_month = event.findAll('div')[0].find('span', class_='event-month').text
                event_date_day = event.findAll('div')[0].find('span', class_='event-day').text
                event_name = event.find('strong').find('a').text
                event_description = 'wo nada'
                event_short_text = 'taki nada'
                event_url = event.find('strong').a['href']
                Event.objects.get_or_create(company=company,
                                            name=event_name,
                                            description=event_description,
                                            short_text=event_short_text,
                                            url=event_url)
                # news fly over like shifaner under the Paris
