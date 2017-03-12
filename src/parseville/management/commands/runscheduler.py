from django.core.management.base import BaseCommand
import schedule
import time


class Command(BaseCommand):
    can_import_settings = True

    def handle(self, *args, **options):
        jobs()


def job():
    print("I'm working...")


def scheduler():
    schedule.every(1).minutes.do(job)
    # schedule.every().hour.do(job)
    # schedule.every().day.at("10:30").do(job)

    while 1:
        schedule.run_pending()
        time.sleep(1)


def jobs():
    print schedule.jobs




