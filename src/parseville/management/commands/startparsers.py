# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from parseville.management.parsers import dou, softserve
from parseville.management.parsers import cogniance

from parseville.management.parsers import trionika


class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
        start(False)


def start(save):
    #   dou.parse_company(save)
    #  softserve.parse_vacancy(save)
       softserve.parse_offices(save)
    #   cogniance.parse_vacancy(save)
    #   trionika.parse_vacancy(save)
