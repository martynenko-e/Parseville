from django.db import models


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
    icon = models.ImageField(upload_to="language", blank=True, null=True)
    show = models.BooleanField(default=False)


class Company(MetaModel):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    short_text = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to="brand", blank=True, null=True)
    url = models.URLField(null=True, blank=True)
    vacancy_parse_url = models.URLField(null=True, blank=True)
    show = models.BooleanField(default=False)
    show_on_main = models.BooleanField(default=False)
    has_parser = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)
    extra = models.TextField(null=True, blank=True)


class Vacancy(MetaModel):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    short_text = models.CharField(max_length=255, blank=True, null=True)
    date_of_publication = models.DateField(blank=True, null=True)
    show = models.BooleanField(default=False)
    show_on_main = models.BooleanField(default=False)
    url = models.URLField(null=True, blank=True)
    company = models.ForeignKey(Company)
    city = models.ForeignKey(City, null=True, blank=True)
    programming_language = models.ForeignKey(ProgrammingLanguage, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    extra = models.TextField(null=True, blank=True)


class UsefulLink(MetaModel):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    short_text = models.CharField(max_length=255, blank=True, null=True)
    show = models.BooleanField(default=False)
    show_on_main = models.BooleanField(default=False)
    url = models.URLField(null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
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
    office = models.ForeignKey(Office, related_name="events")
    date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    short_text = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(null=True, blank=True)


