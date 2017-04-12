from django.db import models
from parseville.settings.base import STATIC_URL


class MetaModel(models.Model):
    def __str__(self):
        return "%s" % self.name.replace(" ", "-")

    def __unicode__(self):
        return u"%s" % self.name.replace(" ", "-")

    class Meta:
        abstract = True


class Country(MetaModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    name_ukr = models.CharField(max_length=200, null=True, blank=True)
    name_rus = models.CharField(max_length=200, null=True, blank=True)
    alias = models.CharField(max_length=200, null=True, blank=True)
    show = models.BooleanField(default=False)


class City(MetaModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    name_ukr = models.CharField(max_length=200, null=True, blank=True)
    name_rus = models.CharField(max_length=200, null=True, blank=True)
    alias = models.CharField(max_length=200, null=True, blank=True)
    show = models.BooleanField(default=False)
    country = models.ForeignKey(Country, related_name="cities", null=True, blank=True)


class ProgrammingLanguage(MetaModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    alias = models.CharField(max_length=200, null=True, blank=True)
    icon = models.ImageField(upload_to="static/images/language", blank=True, null=True)
    show = models.BooleanField(default=False)


class Company(MetaModel):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    short_text = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to="static/images/brand", blank=True, null=True)
    url = models.URLField(null=True, blank=True)
    vacancy_url = models.URLField(null=True, blank=True)
    event_url = models.URLField(null=True, blank=True)
    news_url = models.URLField(null=True, blank=True)
    show = models.BooleanField(default=False)
    show_on_main = models.BooleanField(default=False)
    has_parser = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    extra = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        if self.logo:
            return STATIC_URL + "%s" % self.logo
        else:
            return None


class Vacancy(MetaModel):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    short_text = models.CharField(max_length=255, blank=True, null=True)
    show = models.BooleanField(default=False)
    show_on_main = models.BooleanField(default=False)
    url = models.URLField(null=True, blank=True)
    company = models.ForeignKey(Company)
    city = models.ForeignKey(City, null=True, blank=True)
    programming_language = models.ForeignKey(ProgrammingLanguage, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    extra = models.TextField(null=True, blank=True)


class UsefulLink(MetaModel):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    short_text = models.CharField(max_length=255, blank=True, null=True)
    show = models.BooleanField(default=False)
    show_on_main = models.BooleanField(default=False)
    url = models.URLField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    extra = models.TextField(null=True, blank=True)


class Office(MetaModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    company = models.ForeignKey(Company, related_name="offices")
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    city = models.ForeignKey(City, related_name="offices")


class Event(MetaModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    office = models.ForeignKey(Office, related_name="events", null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    short_text = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(null=True, blank=True)
    upcoming_date = models.DateTimeField(null=True, blank=True)
    company = models.ForeignKey(Company, related_name="events", null=True, blank=True)


class News(MetaModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    short_text = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="static/images/news")
    company = models.ForeignKey(Company, related_name="news")

    def get_absolute_url(self):
        if self.image:
            return STATIC_URL + "%s" % self.image
        else:
            return None


