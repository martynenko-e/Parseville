from django.db import models


class MetaModel(models.Model):
    def __str__(self):
        return self.name.replace(" ", "-")

    class Meta:
        abstract = True


class Country(MetaModel):
    name = models.CharField(max_length=200, null=False, blank=False, db_index=True)
    alias = models.CharField(max_length=200)
    show = models.BooleanField(default=False)


class City(MetaModel):
    name = models.CharField(max_length=200, null=False, blank=False, db_index=True)
    alias = models.CharField(max_length=200)
    show = models.BooleanField(default=False)


class ProgrammingLanguage(MetaModel):
    name = models.CharField(max_length=200, null=False, blank=False, db_index=True)
    alias = models.CharField(max_length=200)
    show = models.BooleanField(default=False)


class Company(MetaModel):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to="company", blank=True, null=True)
    show = models.BooleanField(default=False)
    site_url = models.URLField(null=True, blank=True)
    country = models.ForeignKey(Country)
    city = models.ForeignKey(City)
    show_on_main = models.BooleanField(default=False)


class Vacancy(MetaModel):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    date_of_publication = models.DateField(blank=True, null=True)
    show = models.BooleanField(default=False)
    show_on_main = models.BooleanField(default=False)
    vacancy_url = models.URLField(null=True, blank=True)
    company = models.ForeignKey(Company)
    city = models.ForeignKey(City)
    programming_language = models.ForeignKey(ProgrammingLanguage)


class UsefullLinks(MetaModel):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=False)
    show_on_main = models.BooleanField(default=False)
    url = models.URLField(null=True, blank=True)

