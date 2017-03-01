"""Parseville URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from parseville.views import main, api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main.bootstrap_test, name='bootstrap'),
    url(r'^test/', main.test, name='test'),
    url(r'^index/', main.index, name='index'),
    url(r'^api/init/', api.api_init, name='api_init'),
    url(r'^api/link/(?P<count>[\d]+)?/?', api.api_link, name='api_link'),
    url(r'^api/vacancy/(?P<count>[\d]+)?/?', api.api_vacancy, name='api_vacancy'),
    url(r'^api/company/(?P<count>[\d]+)?/?', api.api_company, name='api_company'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
      + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
