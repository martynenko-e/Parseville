# -*- coding: utf-8 -*-
from django.shortcuts import render
from api import get_company_batch, get_vacancy_batch, get_link_batch

import json


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
    data_init = {
        "company_list": get_company_batch(0),
        "vacancy_list": get_vacancy_batch(0),
        "link_list": get_link_batch(0),
    }
    return render(request, 'marty-index.html', {'data_init': json.dumps(data_init)})

