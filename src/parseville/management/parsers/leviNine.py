# -*- coding: utf-8 -*-
import re
from helper import get_soup_from_url, download_image_parse
from parseville.models import Company, Vacancy, Country, City, Office, News, Event


def parse_vacancy(save):
    soup = get_soup_from_url(
        'https://ukraine.levi9.jobs/open-positions/', save)
    if soup:
        vacancy_elements = soup.find('div', id_="accordion").findAll('div', class_="panel")
        if vacancy_elements:
            for vacancy in vacancy_elements:
                # could be that levi9 have no direct url to vacancy, so below url can be deleted
                vacancy_url = vacancy.find('div', class_="panel-heading").a['href']
                vacancy_title = vacancy.find('div', class_="panel-heading").h4.text
                print vacancy_title
                desc = vacancy.find('div', class_="panel-body").find('div', class_="row").find('div',
                                                                                               class_="col-md-6 info-text")
                print desc
                comp = Company.objects.get(alias='levi9 ukraine')
                print comp.name
                vacancy_obj, created = Vacancy.objects.get_or_create(name=vacancy_title, company=comp)
                vacancy_obj.alias = 'levinine'
                vacancy_obj.description = desc
                vacancy_obj.url = vacancy_url
                vacancy_obj.extra = ' '
                vacancy_obj.save()


def parse_offices(save):
    company = Company.objects.get(alias='levi9 ukraine')
    soup = get_soup_from_url('https://ukraine.levi9.jobs/contact/', False)
    if soup:
        list_of_offices = soup.find('div', id='contact').find('div', class_='row').findAll('div', class_='col-sm-6')
        office_phone = soup.find('div', class_='contact_box_footer') \
            .findAll('div', class_='col-md-4 col-sm-6')[3].a['href']
        # print office_phone -->
        # print list_of_offices --> ok
        if list_of_offices:
            for office in list_of_offices:
                office_info = office.find('div', class_='info')
                # print office_info --> ok
                office_city = office_info.findAll('p')[0].text
                # print office_city --> ok
                if office_city == 'Kyiv':
                    office_lat = 50.395083
                    office_lng = 30.478810000000067
                    office_email = 'HR-Kiev@levi9.com'
                else:
                    print 'no Kyiv office found'
                if office_city == 'Lviv':
                    office_lat = 49.841733
                    office_lng = 24.025429
                    office_email = 'HR-Lviv@levi9.com'
                else:
                    print 'no Lviv office found'
                city = City.objects.get(name=office_city)
                office_name = office_info.findAll('p')[1].text
                # print office_name --> ok
                office_address = office_info.findAll('p')[2].text
                Office.objects.get_or_create(name=office_name,
                                             city=city,
                                             company=company,
                                             latitude=office_lat,
                                             longitude=office_lng,
                                             address=office_address,
                                             phone=office_phone,
                                             email=office_email)


def parse_events(save):
    company = Company.objects.get(alias='levi9 ukraine')
    soup = get_soup_from_url(
        'https://ukraine.levi9.jobs/news/', save)
    if soup:
        event_blocks = soup.find('div', id='news_loop').findAll('div', class_='col-md-4')
        if event_blocks:
            for event in event_blocks:
                title = event.find('h3').find('a').text
                # link = get_soup_from_url(event.a['href'], save)
                link = event.find('a')['href']
                #date = event.find('h6').text
                # if link.find('div', class_='text_exposed_show'):
                #   office = link.find('div', class_='text_exposed_show').find('p')
                # else:
                #    office = 'we don\'t know where event will take place'
                Event.objects.get_or_create(company=company,
                                            name=title,
                                            description=" ",
                                            short_text=" ",
                                            url=link)

# News are included to Events in Levi Nine and there is no flag in order to separate them
