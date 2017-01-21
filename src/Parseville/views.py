from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from django.http import JsonResponse


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


@csrf_exempt
def api_link(request):
    data = []
    link_objects = UsefullLinks.objects.all()
    for link_obj in link_objects:
        data.append({
            "name": link_obj.name,
            "url": link_obj.url,
            "description": link_obj.description,
        })
    return JsonResponse(data, safe=False)


@csrf_exempt
def api_company(request):
    data = []
    company_objects = Company.objects.all()
    for company_obj in company_objects:
        data.append({
            "name": company_obj.name,
            "description": company_obj.description,
            "site_url": company_obj.site_url,
            "country": company_obj.country.name,
            "city": company_obj.city.name,
        })
    return JsonResponse(data, safe=False)


@csrf_exempt
def api_vacancy(request):
    data = []
    vacancy_objects = Vacancy.objects.all()
    for vacancy_obj in vacancy_objects:
        data.append({
            "name": vacancy_obj.name,
            "url": vacancy_obj.vacancy_url,
            "description": vacancy_obj.description,
            "company": vacancy_obj.company.name,
            # "city": vacancy_obj.city.name,
            "programming_language": vacancy_obj.programming_language.name,
        })
    return JsonResponse(data, safe=False)