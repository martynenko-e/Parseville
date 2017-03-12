# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from parseville.models import City, Country, ProgrammingLanguage, UsefulLink


class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
        init()


def init():
    country_obj, created = Country.objects.get_or_create(name="Ukraine", alias="ukraine", show=True)
    City.objects.get_or_create(name="Kiev", alias="kiev", show=True, country=country_obj)
    ProgrammingLanguage.objects.get_or_create(name="JavaScript", alias="javascript", show=True)
    ProgrammingLanguage.objects.get_or_create(name="Java", alias="java", show=True)
    ProgrammingLanguage.objects.get_or_create(name="Python", alias="python", show=True)
    ProgrammingLanguage.objects.get_or_create(name="C++", alias="c++", show=True)
    ProgrammingLanguage.objects.get_or_create(name="Android", alias="android", show=True)
    ProgrammingLanguage.objects.get_or_create(name="HTML", alias="html", show=True)
    ProgrammingLanguage.objects.get_or_create(name="CSS", alias="css", show=True)
    UsefulLink.objects.get_or_create(name="Tproger",
                                     alias="tproger",
                                     url="https://tproger.ru/",
                                     short_text="Типичный программист — cоздано программистами для программистов",
                                     show=True,
                                     show_on_main=True)
