# -*- coding: utf-8 -*-
import json

from datetime import datetime
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from parseville.models import *

BATCH_SIZE = 5


@csrf_exempt
def api_init(request):
    data = {
        "company_list": get_company_batch(0),
        "vacancy_list": get_vacancy_batch(0),
        "link_list": get_link_batch(0),
    }
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response["Access-Control-Allow-Origin"] = '*'
    return response


@csrf_exempt
def api_link(request, count=1):
    if not count:
        count = 1
    else:
        count = int(count)
    data = {
        "link_list": get_link_batch(count)
    }
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response["Access-Control-Allow-Origin"] = '*'
    return response


@csrf_exempt
def api_company(request, count=1):
    if not count:
        count = 1
    else:
        count = int(count)
    data = {"companies": get_company_batch(count)}
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response["Access-Control-Allow-Origin"] = '*'
    return response


@csrf_exempt
def api_vacancy(request, count="1"):
    if not count:
        count = 1
    else:
        count = int(count)
    data = {
        "vacancies": get_vacancy_batch(count)
    }
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response["Access-Control-Allow-Origin"] = '*'
    return response


@csrf_exempt
def api_event(request, count="1"):
    if not count:
        count = 1
    else:
        count = int(count)
    data = {
        "events": get_event_batch(count)
    }
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response["Access-Control-Allow-Origin"] = '*'
    return response


@csrf_exempt
def api_article(request, count="1"):
    if not count:
        count = 1
    else:
        count = int(count)
    data = {
        "news": get_article_batch(count)
    }
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response["Access-Control-Allow-Origin"] = '*'
    return response


@csrf_exempt
def api_offices(request):
    data = {
        "office_list": get_office_batch("")
    }
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response["Access-Control-Allow-Origin"] = '*'
    return response


@csrf_exempt
def api_get_offices(request):
    data = {
        "office_list": get_office_batch("kiev")
    }
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response["Access-Control-Allow-Origin"] = '*'
    return response


def get_company_batch(count):
    company_query_set = Company.objects.filter(show=True).order_by('-date')[BATCH_SIZE * count:BATCH_SIZE * count + BATCH_SIZE] \
        .values_list("id",
                     "name",
                     "description",
                     "logo",
                     "date",
                     "url",
                     "short_text")

    data = map(lambda element: {
        "id": element[0],
        "name": element[1],
        "description": element[2],
        "image": "/" + element[3],
        "date": element[4].strftime("%B %d, %Y"),
        "url": element[5],
        "short_text": element[6],
    }, company_query_set)
    return data


def get_vacancy_batch(count):
    vacancy_query_set = Vacancy.objects.filter(show=False,
                                               date__isnull=False,
                                               date__lte=datetime.now()
                                               ).order_by('date')[BATCH_SIZE * count:BATCH_SIZE * count + BATCH_SIZE] \
        .values_list("id",
                     "name",
                     "description",
                     "date",
                     "company__name",
                     "programming_language",
                     "url",
                     "short_text")

    data = map(lambda element: {
        "id": element[0],
        "name": element[1],
        "description": element[2],
        "date": element[3].strftime("%B %d, %Y"),
        "company_name": element[4],
        "p_language": element[5],
        "url": element[6],
        "short_text": element[7],
    }, vacancy_query_set)

    return data


def get_link_batch(count):
    link_query_set = UsefulLink.objects.filter(show=False,
                                               date__isnull=False,
                                               date__lte=datetime.now()
                                               ).order_by('-date')[BATCH_SIZE * count:BATCH_SIZE * count + BATCH_SIZE]. \
        values_list("id",
                    "name",
                    "short_text",
                    "date",
                    "url")
    data = map(lambda element: {
        "id": element[0],
        "name": element[1],
        "short_text": element[2],
        "date": element[3].strftime("%B %d, %Y"),
        "url": element[4],
    }, link_query_set)
    return data


def get_event_batch(count):
    event_query_set = Event.objects.filter(
                                           date__isnull=False,
                                           date__lte=datetime.now()
                                           ).order_by('-date')[BATCH_SIZE * count:BATCH_SIZE * count + BATCH_SIZE]. \
        values_list("id",
                    "name",
                    "short_text",
                    "description",
                    "url",
                    "date",
                    "company__name")
    data = map(lambda element: {
        "id": element[0],
        "name": element[1],
        "short_text": element[2],
        "description": element[3],
        "url": element[4],
        "date": element[5].strftime("%B %d, %Y"),
        "company_name": element[6],
    }, event_query_set)
    return data


def get_article_batch(count):
    article_query_set = News.objects.filter(
                                            date__isnull=False,
                                            date__lte=datetime.now()
                                            ).order_by('-date')[BATCH_SIZE * count:BATCH_SIZE * count + BATCH_SIZE]. \
        values_list("id",
                    "name",
                    "short_text",
                    "description",
                    "url",
                    "image",
                    "date",
                    "company__name")
    data = map(lambda element: {
        "id": element[0],
        "name": element[1],
        "short_text": element[2],
        "description": element[3],
        "url": element[4],
        "image": "/" + element[5],
        "date": element[6].strftime("%B %d, %Y"),
        "company_name": element[7],
    }, article_query_set)
    return data


def get_office_batch(city):
    if (city):
        office_query_set = Office.objects.filter(city__alias=city).values_list(
                "name",
                "address",
                "latitude",
                "longitude",
                "phone",
                "company__name"
        )
    else:
        office_query_set = Office.objects.filter().values_list(
                "name",
                "address",
                "latitude",
                "longitude",
                "phone",
                "company__name"
        )

    data = map(lambda element: {
        "name": element[0],
        "address": element[1],
        "lat": element[2],
        "lng": element[3],
        "phone": element[4],
        "company": element[5],
    }, office_query_set)
    return data
