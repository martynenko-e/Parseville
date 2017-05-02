# -*- coding: utf-8 -*-
from django.shortcuts import render
from parseville.models import Vacancy, Company, Event, News, Office
from parseville.views.api import get_company_batch, get_vacancy_batch, get_event_batch, get_article_batch
import json

ROWS_IN_BLOCK = 10
NEWS_BLOCK = 5
SITE_NAME = 'Parseville'


def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html with the data in the context variable
    return render(
            request,
            'index.html',
            context={'header': 'header'},
    )


def marty(request):
    latest_vacancies = map(lambda vacancy: {
        'id': vacancy.id,
        "name": vacancy.name,
        "short_text": vacancy.short_text,
        "description": vacancy.description,
        "date": vacancy.date.strftime("%B %d, %Y"),
        "company_name": vacancy.get_company_name(),
    }, Vacancy.objects.filter().order_by("-date")[:ROWS_IN_BLOCK])

    show_on_main_companies = map(lambda company: {
        'id': company.id,
        "name": company.name,
        "short_text": company.short_text,
        "description": company.description,
        "image": company.get_absolute_url(),
        "date": company.date.strftime("%B %d, %Y"),
    }, Company.objects.filter(show_on_main=True).order_by("-date")[:ROWS_IN_BLOCK])

    latest_events = map(lambda event: {
        "id": event.id,
        "name": event.name,
        "short_text": event.short_text,
        "description": event.description,
        "date": event.date.strftime("%B %d, %Y"),
        "company_name": event.get_company_name(),
    }, Event.objects.filter().order_by("-date")[:ROWS_IN_BLOCK])

    latest_news = map(lambda new: {
        "id": new.id,
        "name": new.name,
        "short_text": new.short_text,
        "description": new.description,
        "date": new.date.strftime("%B %d, %Y"),
        "image": new.get_absolute_url(),
        "visit_url": new.url,
        "company_name": new.get_company_name(),
    }, News.objects.filter().order_by("-date")[:NEWS_BLOCK])

    data = {
        "companies": show_on_main_companies,
        "vacancies": latest_vacancies,
        "events": latest_events,
        "news": latest_news,
    }

    return render(request, 'index.html', {
        'latest_vacancies': latest_vacancies,
        'show_on_main_companies': show_on_main_companies,
        'latest_events': latest_events,
        'latest_news': latest_news,
        'events_url': "/events/",
        'event_count': Event.objects.filter().count(),
        'vacancies_url': "/vacancies/",
        'vacancy_count': Vacancy.objects.filter().count(),
        'companies_url': "/companies/",
        'company_count': Company.objects.filter().count(),
        'news_url': "/news/",
        'news_count': News.objects.filter().count(),
        'title': SITE_NAME,
        'data': json.dumps(data),
        'index_data': data
    })


def vacancies(request):
    data = get_vacancy_batch(0)
    init_data = {
        'vacancies': data,
    }
    return render(request, 'all-elements.html', {
        'title': SITE_NAME + ' - all vacancies',
        'data': data,
        'type': 'vacancy',
        'init_data': json.dumps(init_data)
    })


def companies(request):
    data = get_company_batch(0)
    offices = map(lambda office: {
        "id": office.id,
        "name": office.name,
        "address": office.address,
        "company": office.company.name,
        "phone": office.phone,
        "email": office.email,
        "latitude": office.latitude,
        "longitude": office.longitude,
        "city": office.city.name
    }, Office.objects.filter())
    init_data = {
        'companies': data,
        'offices': offices
    }
    return render(request, 'all-elements.html', {
        'title': SITE_NAME + ' - all companies',
        'data': data,
        'init_data': json.dumps(init_data),
        'type': 'company'
    })


def events(request):
    data = get_event_batch(0)
    init_data = {
        'events': data,
    }
    return render(request, 'all-elements.html', {
        'title': SITE_NAME + ' - all events',
        'data': data,
        'type': 'event',
        'init_data': json.dumps(init_data),
    })


def news(request):
    data = get_article_batch(0)
    init_data = {
        'news': data,
    }
    return render(request, 'all-elements.html', {
        'title': SITE_NAME + ' - all news',
        'data': data,
        'type': 'article',
        'init_data': json.dumps(init_data)
    })


def custom_page_not_found_view(request):
    return render(request, "404.html", status=404)
