# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from parseville.models import *


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


def test(request):
    return render(request, 'test.html', {})


def bootstrap_test(request):
    return render(request, 'marty-index.html', {
    })


@csrf_exempt
def api_init(request):
    company_query_set = Company.objects.filter(show=True).order_by('added_date')[:3].values_list("id", "name",
                                                                                                 "description", "logo", "site_url")
    vacancy_query_set = Vacancy.objects.filter(show=True).order_by('added_date')[:3].values_list("id", "name",
                                                                                                 "description", "date_of_publication", "company__name", "programming_language")
    link_query_set = UsefullLink.objects.filter(show=True).order_by('added_date')[:3].values_list("id", "name", "description", "url")

    data = {
        "company_list": map(lambda element: {
            "id": element[0],
            "name": element[1],
            "description": element[2],
            "logo": "/media/" + element[3],
            "site_url": element[4],
        }, company_query_set),
        "vacancy_list": map(lambda element: {
            "id": element[0],
            "name": element[1],
            "description": element[2],
            "pub_date": element[3],
            "company_name": element[4],
            "p_language": element[5],
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
def api_link(request):
    data = []
    link_objects = UsefullLink.objects.filter(show=True)
    for link_obj in link_objects:
        data.append({
            "id": "link-" + link_obj.id,
            "name": link_obj.name,
            "url": link_obj.url,
            "description": link_obj.description,
            "added_date": link_obj.added_date,
        })
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response["Access-Control-Allow-Origin"] = '*'
    return response


@csrf_exempt
def api_company(request):
    data = []
    company_objects = Company.objects.filter(show=True)
    for company_obj in company_objects:
        data.append({
            "id": "company-" + company_obj.id,
            "name": company_obj.name,
            "description": company_obj.description,
            "site_url": company_obj.site_url,
            "country": company_obj.country,
            "office": company_obj.office,
            "logo": company_obj.logo.url,
            "added_date": company_obj.added_date,
        })
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response["Access-Control-Allow-Origin"] = '*'
    return response


@csrf_exempt
def api_vacancy(request):
    data = []
    vacancy_objects = Vacancy.objects.filter(show=True)
    for vacancy_obj in vacancy_objects:
        data.append({
            "id": "vacancy-" + vacancy_obj.id,
            "name": vacancy_obj.name,
            "url": vacancy_obj.vacancy_url,
            "description": vacancy_obj.description,
            "company": vacancy_obj.company.name,
            "city": vacancy_obj.city,
            "programming_language": vacancy_obj.programming_language,
            "added_date": vacancy_obj.added_date,
        })

    response = HttpResponse(json.dumps(data), content_type='application/json')
    response["Access-Control-Allow-Origin"] = '*'
    return response
