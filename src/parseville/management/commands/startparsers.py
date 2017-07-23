# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from parseville.management.parsers import dou, softserve
from parseville.management.parsers import cogniance
from parseville.management.parsers import leviNine
from parseville.management.parsers import trionika
from parseville.management.parsers import lohika
from parseville.management.parsers import ciklum


class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
        start(False)


def start(save):
    # dou.parse_company(save)
    try:
        leviNine.parse_vacancy(False)
        leviNine.parse_events(False)
        leviNine.parse_offices(False)
        # softserve.parse_events(save)
        # softserve.parse_news(save)
        # softserve.parse_vacancy(save)
        # softserve.parse_offices(save)
        # cogniance.parse_vacancy(save)
        # cogniance.parse_offices(save)
        # cogniance.parse_events(save)
        # trionika.parse_vacancy(save)
        # trionika.parse_offices(save)
        # trionika.parse_events(save)
        # lohika.parse_vacancy(save)
        # lohika.parse_offices(save)
        # lohika.parse_events(save)
        # ciklum.parse_vacancy(save)
    except Exception as e:
        print "Problem: %s" % e
