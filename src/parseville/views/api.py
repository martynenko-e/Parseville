# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from parseville.models import *


@csrf_exempt
def api_init(request):
    company_query_set = Company.objects.filter(show=True).order_by('added_date')[:3].values_list("id",
                                                                                                 "name",
                                                                                                 "description",
                                                                                                 "logo",
                                                                                                 "site_url",
                                                                                                 "short_text")
    vacancy_query_set = Vacancy.objects.filter(show=True).order_by('added_date')[:3].values_list("id",
                                                                                                 "name",
                                                                                                 "description",
                                                                                                 "date_of_publication",
                                                                                                 "company__name",
                                                                                                 "programming_language",
                                                                                                 "vacancy_url",
                                                                                                 "short_text")
    link_query_set = UsefullLink.objects.filter(show=True).order_by('added_date')[:3].values_list("id",
                                                                                                  "name",
                                                                                                  "description",
                                                                                                  "url")

    data = {
        "company_list": map(lambda element: {
            "id": element[0],
            "name": element[1],
            "description": element[2],
            "logo": "/media/" + element[3],
            "site_url": element[4],
            "short_text": element[5],
        }, company_query_set),
        "vacancy_list": map(lambda element: {
            "id": element[0],
            "name": element[1],
            "description": element[2],
            "pub_date": element[3],
            "company_name": element[4],
            "p_language": element[5],
            "url": element[6],
            "short_text": element[7],
        }, vacancy_query_set),
        "link_list": map(lambda element: {
            "id": element[0],
            "name": element[1],
            "description": element[2],
            "url": element[3],
        }, link_query_set),
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
    link_query_set = UsefullLink.objects.filter(show=True).order_by('added_date')[3 * count:3 * count + 3].values_list("id",
                                                                                                  "name",
                                                                                                  "description",
                                                                                                  "url")
    data = {
        "link_list": map(lambda element: {
            "id": element[0],
            "name": element[1],
            "description": element[2],
            "url": element[3],
        }, link_query_set),
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
    company_query_set = Company.objects.filter(show=True).order_by('added_date')[3 * count:3 * count + 3].values_list("id",
                                                                                                 "name",
                                                                                                 "description",
                                                                                                 "logo",
                                                                                                 "site_url",
                                                                                                 "short_text")

    data = {"company_list": map(lambda element: {
                "id": element[0],
                "name": element[1],
                "description": element[2],
                "logo": "/media/" + element[3],
                "site_url": element[4],
                "short_text": element[5],
        }, company_query_set)}
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response["Access-Control-Allow-Origin"] = '*'
    return response


@csrf_exempt
def api_vacancy(request, count="1"):
    if not count:
        count = 1
    else:
        count = int(count)
    vacancy_query_set = Vacancy.objects.filter(show=True).order_by('added_date')[3 * count:3 * count + 3].values_list("id",
                                                                                                 "name",
                                                                                                 "description",
                                                                                                 "date_of_publication",
                                                                                                 "company__name",
                                                                                                 "programming_language",
                                                                                                 "vacancy_url",
                                                                                                 "short_text")

    data = {
        "vacancy_list": map(lambda element: {
            "id": element[0],
            "name": element[1],
            "description": element[2],
            "pub_date": element[3],
            "company_name": element[4],
            "p_language": element[5],
            "url": element[6],
            "short_text": element[7],
        }, vacancy_query_set),
    }
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response["Access-Control-Allow-Origin"] = '*'
    return response
