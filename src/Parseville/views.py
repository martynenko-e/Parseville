from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *


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
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response["Access-Control-Allow-Origin"] = '*'
    return response


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
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response["Access-Control-Allow-Origin"] = '*'
    return response


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
            "city": vacancy_obj.city.name,
            "programming_language": vacancy_obj.programming_language.name,
        })

    response = HttpResponse(json.dumps(data), content_type='application/json')
    response["Access-Control-Allow-Origin"] = '*'
    return response


def add_test_data(request):
    obj_city, created = City.objects.get_or_create(
        name='Kyiv',
        alias='kyiv',
        show=True,
    )

    obj_country, created = Country.objects.get_or_create(
        name='Ukraine',
        alias='ukraine',
        show=True,
    )

    obj_company, created = Company.objects.get_or_create(
        name='BETLAB',
        alias='betlab',
        description="BETLAB is Ukrainian Software product company for Sportsbook sphere."
                    "We started at 2014 in Kiev."
                    "Our strong and ambitious goal is to deliver the best breed of cross cultural experiences our team is packed with. "
                    "Growing our products comfortable for users and bringing best user experience practises to our products."
                    "We create BETLAB Platform for Sportsbook sphere which consists of four products:"
                    "— Channels solution is working to improve playing experience in betshops for both players and staff in different cultural surroundings. Our special web, desktop, mobile applications."
                    "— Math Product. We develop and implement predictive models for sport events including their validation and monitoring of such models."
                    "— Sports Products. Highly scalable and flexible sportsbetting platform developed to simplify and automatize the process of running a betting activity."
                    "— Trading Tools Products. Workplace for trader to control and manage sport real-time events."
                    "— Core product. Accounts managing system for business users. Back office, smart wallet, risk management system, payment system."
                    "We are different:"
                    "— Our processes are based on Agile principles;"
                    "— Self-organization for generating a greater customer value;"
                    "— Respect to our people;"
                    "— Walk with customers;"
                    "— Driven by Innovations.",
        show=True,
        site_url="betlab.com",
        country=obj_country,
        city=obj_city,
        show_on_main=True,

    )

    obj_lang, created = ProgrammingLanguage.objects.get_or_create(
        name='JavaScript',
        alias='javasript',
        show=True,
    )

    obj_vacancy, created = Vacancy.objects.get_or_create(
        name='Middle Front-End Developer (Sport Product)',
        alias='middle_front_end_developer',
        description="Необхідні навики"
                    "— Strong Web development background, at least 3 years;"
                    "— Strong knowledge in native JS;"
                    "— Proven experience with one of modern framework (Angular, React, etc.);"
                    "— Experience with one of build systems (Webpack, Gulp, Grunt);"
                    "— Work experience with RESTful API;"
                    "— VCS git"
                    "Буде плюсом"
                    "—React;"
                    "— Webpack;"
                    "— Es6;"
                    "— NodeJS;"
                    "— WebSockets"
                    "Пропонуємо"
                    "As well as a competitive salary there are a range of benefits including:"
                    "-Fully paid sick leaves and 20 working days paid vacation;"
                    "-Great opportunity to take part in unique Ukrainian Sportsbook product development;"
                    "-Team of passionate professionals with experience exchange;"
                    "-Paid trainings, conferences, professional library and career and proficiency development plans;"
                    "-Team building events;"
                    "-Paid sport trainings/medical insurance;"
                    "-Sandwiches, juices, cookies, fruits and many-many more..."
                    "Обов’язки"
                    "— Front-end development in one of web products;"
                    "— Applications architecture design;"
                    "— Code review.",
        show=True,
        vacancy_url="https://jobs.dou.ua/companies/betlab/vacancies/35274/",
        company=obj_company,
        city=obj_city,
        show_on_main=True,
        programming_language=obj_lang,
    )