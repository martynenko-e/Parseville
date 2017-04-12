# -*- coding: utf-8 -*-
from django.shortcuts import render
from parseville.models import Vacancy, Company, Event, News
from parseville.views.api import get_company_batch, get_vacancy_batch, get_link_batch
import json

ROWS_IN_BLOCK = 10
NEWS_BLOCK = 5


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
        "description": vacancy.short_text,
        "date": vacancy.date,
        "company": vacancy.company.name,
    }, Vacancy.objects.filter().order_by("-date")[:ROWS_IN_BLOCK])

    show_on_main_companies = map(lambda company: {
        'id': company.id,
        "name": company.name,
        "description": company.short_text,
        "image": company.get_absolute_url(),
        "date": company.date,
    }, Company.objects.filter(show_on_main=True).order_by("-date")[:ROWS_IN_BLOCK])

    latest_events = map(lambda event: {
        "name": event.name,
        "description": event.short_text,
        "date": event.date,
    }, Event.objects.filter().order_by("-date")[:ROWS_IN_BLOCK])

    latest_news = map(lambda new: {
        "name": new.name,
        "description": new.short_text,
        "date": new.date,
        "image": new.get_absolute_url(),
        "visit_url": new.url,
    }, News.objects.filter().order_by("-date")[:NEWS_BLOCK])

    data = {
        "company_list": get_company_batch(0),
        "vacancy_list": get_vacancy_batch(0),
        "link_list": get_link_batch(0),
    }

    return render(request, 'marty-index.html', {
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
        'title': 'Parseville',
        'data': json.dumps(data)
    })


def vacancies(request):
    data = map(lambda vacancy: {
        "name": vacancy.name,
        "description": vacancy.short_text,
        "date": vacancy.date,
        "company": vacancy.company.name,
    }, Vacancy.objects.filter().order_by("-date"))
    return render(request, 'temp.html', {
        'title': 'All vacancies',
        'data': data,
    })


def companies(request):
    data = map(lambda company: {
        "name": company.name,
        "description": company.short_text,
        "image": company.get_absolute_url(),
        "date": company.date,
    }, Company.objects.filter().order_by("-date"))
    return render(request, 'temp.html', {
        'title': 'All companies',
        'data': data,
    })


def events(request):
    data = map(lambda event: {
        "name": event.name,
        "description": event.short_text,
        "date": event.date,
    }, Event.objects.filter().order_by("-date"))
    return render(request, 'temp.html', {
        'title': 'All events',
        'data': data,
    })


def news(request):
    data = map(lambda new: {
        "name": new.name,
        "description": new.short_text,
        "date": new.date,
        "image": new.get_absolute_url(),
        "visit_url": new.url,
    }, News.objects.filter().order_by("-date"))
    return render(request, 'temp.html', {
        'title': 'All news',
        'data': data,
    })


def custom_page_not_found_view(request):
    return render(request, "404.html", status=404)
