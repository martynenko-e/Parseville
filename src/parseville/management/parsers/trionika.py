# -*- coding: utf-8 -*-
import re
from helper import get_soup_from_url
from parseville.models import Company, Vacancy, Country, City, Office, Event


def parse_vacancy(save):
    company = Company.objects.filter(alias='trionika')
    if company.count() > 0:
        company = company[0]
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
                    Vacancy.objects.get_or_create(name=title.text,
                                                  company=company,
                                                  alias=re.sub(r'[^a-zA-Z]+', "-", title.text.lower()),
                                                  )


def parse_offices(save):
    company = Company.objects.get(alias='trionika')
    soup = get_soup_from_url('http://trionika.com/', save)
    if soup:
        kiev_office_address = soup.find('div', class_='address')
        office_name = kiev_office_address.find('div', class_='trion-link').text
        office_address = kiev_office_address.text[51:77]
        city = City.objects.get(name='Kyiv')
        office_phone = kiev_office_address.findAll('a')[0].text
        office_email = kiev_office_address.findAll('a')[1].text[6:]
        Office.objects.get_or_create(name=office_name,
                                     city=city,
                                     company=company,
                                     latitude=02,
                                     longitude=03,
                                     address=office_address,
                                     phone=office_phone,
                                     email=office_email)


def parse_events(save):
    company = Company.objects.get(alias='trionika')
    soup = get_soup_from_url('http://trionika.com/', save)
    if soup:
        slider = soup.find('div', id='project-slider')
        if slider:
            events = slider.find('div', id='owl-events').findAll('div', class_='item event')

            '''
            if events:
                events_list = events.findll('div', class_='owl-item')
                if events_list:
                    for event in events_list:
                        event_item = event \
                            .find('div', class_='item') \
                            .find('div', class_='table_holder')
                        event_date = event_item \
                            .findAll('div', class_='table_cell')[0] \
                            .find('div', class_='hero-profile') \
                            .find('div', class_='date-line') \
                            .find('span', class_='club').text

                        event_name = event_item.findAll('div', class_='table_cell')[1] \
                            .find('div', class_='event-description') \
                            .find('div', class_='event-title').text
                        event_description = event_item.findAll('div', class_='table_cell')[1] \
                            .find('div', class_='event-description') \
                            .find('div', class_='event-body').find('p').text
                        event_short_text = 'short text'
                        url = event_item.findAll('div', class_='table_cell')[1] \
                            .find('div', class_='event-description') \
                            .find('div', class_='regista').a['href']
                        Event.objects.get_or_create(company=company,
                                                    name=event_name,
                                                    date=event_date,
                                                    description=event_description,
                                                    short_text=event_short_text,
                                                    url=url)'''
