# -*- coding: utf-8 -*-
import re
import urllib, json

from dateutil import parser
from helper import get_soup_from_url
from parseville.models import Company, Vacancy, Country, City, Event, Office, News


def parse_vacancy(save):
    company = Company.objects.get(alias='lohika')
    url = 'https://cube.lohika.com/0/ServiceModel/JobPosting.svc/vacancies?page=1&locations=&categories='
    response = urllib.urlopen(url)
    file_with_vacancies = json.loads(response.read())
    vacancies = file_with_vacancies['vacancies']
    for vacancy in vacancies:
        print vacancy['title']
        name = vacancy['title']
        description = vacancy['jobPurpose'].encode('utf-8') + '\n' \
                      + 'Optional knowledge: %s ' % vacancy['optionalKnowledge'] + '\n' \
                      + 'Required knowledge: %s' % vacancy['requiredKnowledge']
        # possibly below short_text need to be commented
        short_text1 = 'if vacancy is hot ==> {vacancy}'.format(vacancy=vacancy['isHot'])
        url = vacancy['recruiters']
        date = vacancy['publishedDate']
        programming_language = vacancy['tags']
        vacancy_obj, created = Vacancy.objects.get_or_create(name=name, company=company)
        vacancy_obj.alias = re.sub(" ", "-", name.lower())
        vacancy_obj.description = description
        vacancy_obj.url = url
        vacancy_obj.extra = short_text1
        vacancy_obj.date = date
        vacancy_obj.save()


# parse.html is empty. nothing to parse
def parse_offices(save):
    company = Company.objects.get(alias='lohika')
    Office.objects.get_or_create(name='Kiev office',
                                 city='Kiev',
                                 company=company,
                                 latitude=50.434043,
                                 longiitude=30.509147,
                                 address='35 Zhylianska Street,5 floor',
                                 phone='0445938080',
                                 email='job_kyiv@lohika.com')


def parse_events(save):
    company = Company.objects.get(alias='lohika')
    url = 'http://www.lohika.com.ua/api/news?page=1&locations=all&categories=all'
    response = urllib.urlopen(url)
    file_with_events = json.loads(response.read())
    events = file_with_events['results']
    for event in events:
        print event['title']
        name = event['title']
        date = parser.parse(event['publishedDate'])
        description = event['content'].encode('utf-8')
        short_text = event['slug']
        # we have a category of event ala dev, management, good to have somewhere saved
        Event.objects.get_or_create(company=company,
                                    name=name,
                                    date=date,
                                    description=description,
                                    short_text=short_text)
