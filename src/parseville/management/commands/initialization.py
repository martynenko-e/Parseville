# -*- coding: utf-8 -*-
import re
from django.core.management.base import BaseCommand

from parseville.models import City, Country, ProgrammingLanguage


class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
        init()


def init():
    city_obj, created = City.objects.get_or_create(name="Kiev", alias="kiev", show=True)
    country_obj, created = Country.objects.get_or_create(name="Ukraine", alias="ukraine", show=True)
    prog_obj_1, created = ProgrammingLanguage.objects.get_or_create(name="JavaScript", alias="javascript", show=True)
    prog_obj_2, created = ProgrammingLanguage.objects.get_or_create(name="Java", alias="java", show=True)
    prog_obj_3, created = ProgrammingLanguage.objects.get_or_create(name="Python", alias="python", show=True)
    prog_obj_4, created = ProgrammingLanguage.objects.get_or_create(name="C++", alias="c++", show=True)
    prog_obj_5, created = ProgrammingLanguage.objects.get_or_create(name="Android", alias="android", show=True)
    prog_obj_6, created = ProgrammingLanguage.objects.get_or_create(name="HTML", alias="html", show=True)
    prog_obj_7, created = ProgrammingLanguage.objects.get_or_create(name="CSS", alias="css", show=True)