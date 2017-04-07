# -*- coding: utf-8 -*-
from django.shortcuts import render
from parseville.models import Vacancy, Company, Event, News

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
    # TODO get 20 latest vacancies, adjustable in settings
    # TODO company with show_on_main
    # TODO useful links
    # TODO upcoming events
    # TODO news?

    latest_vacancies = map(lambda vacancy: {
        "name": vacancy.name,
        "description": vacancy.short_text,
        "date": vacancy.date,
        "company": vacancy.company.name,
    }, Vacancy.objects.filter().order_by("-date")[:ROWS_IN_BLOCK])

    show_on_main_companies = map(lambda company: {
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
        'title': 'Parseville'
    })


def vacancies(request):
    return render(request, 'temp.html', {'message': 'Coming soon! There will be list of all vacancies!'})


def companies(request):
    return render(request, 'temp.html', {'message': 'Coming soon! There will be list of all companies!'})


def events(request):
    return render(request, 'temp.html', {'message': 'Coming soon! There will be list of all events!'})


def news(request):
    return render(request, 'temp.html', {'message': 'Coming soon! There will be list of all news!'})

