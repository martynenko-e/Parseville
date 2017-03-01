# -*- coding: utf-8 -*-
from django.shortcuts import render

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
    return render(request, 'index.html', {
    })

