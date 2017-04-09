# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from parseville.models import City, Country, ProgrammingLanguage, UsefulLink


class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
        # hello_world()
        init()


def init():
    ProgrammingLanguage.objects.get_or_create(name="JavaScript", alias="javascript", show=True)
    ProgrammingLanguage.objects.get_or_create(name="Java", alias="java", show=True)
    ProgrammingLanguage.objects.get_or_create(name="Python", alias="python", show=True)
    ProgrammingLanguage.objects.get_or_create(name="C++", alias="c++", show=True)
    ProgrammingLanguage.objects.get_or_create(name="Android", alias="android", show=True)
    ProgrammingLanguage.objects.get_or_create(name="HTML", alias="html", show=True)
    ProgrammingLanguage.objects.get_or_create(name="CSS", alias="css", show=True)
    ProgrammingLanguage.objects.get_or_create(name="Go", alias="go", show=True)
    UsefulLink.objects.get_or_create(name="Tproger",
                                     alias="tproger",
                                     url="https://tproger.ru/",
                                     short_text="Типичный программист — cоздано программистами для программистов",
                                     show=True,
                                     show_on_main=True)
    UsefulLink.objects.get_or_create(name="Proglib",
                                     alias="proglig",
                                     url="https://proglib.io/",
                                     short_text="Библиотека программиста | Материалы по всему, что может быть",
                                     show=True,
                                     show_on_main=True)
    UsefulLink.objects.get_or_create(name="Dou",
                                     alias="dou",
                                     url="https://dou.ua/",
                                     short_text="Онлайн-сообщество разработчиков программного обеспечения",
                                     show=True,
                                     show_on_main=True)


def hello_world():
    # print "Hello from cron tab 2"
    ProgrammingLanguage.objects.get_or_create(name="Django", alias="django", show=True)
