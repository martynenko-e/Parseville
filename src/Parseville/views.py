from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def proxy(request):
    pass


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