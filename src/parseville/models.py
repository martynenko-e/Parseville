from django.db import models


class MetaModel(models.Model):
    def __str__(self):
        return "%s" % self.name.replace(" ", "-")

    def __unicode__(self):
        return u"%s" % self.name.replace(" ", "-")

    class Meta:
        abstract = True


class Country(MetaModel):
    name = models.CharField(max_length=200, null=False, blank=False, db_index=True)
    alias = models.CharField(max_length=200, null=False, blank=False)
    show = models.BooleanField(default=False)


class City(MetaModel):
    name = models.CharField(max_length=200, null=False, blank=False, db_index=True)
    alias = models.CharField(max_length=200, null=False, blank=False)
    show = models.BooleanField(default=False)


class ProgrammingLanguage(MetaModel):
    name = models.CharField(max_length=200, null=False, blank=False, db_index=True)
    alias = models.CharField(max_length=200, null=False, blank=False)
    icon = models.ImageField(upload_to="language", blank=True, null=True)
    show = models.BooleanField(default=False)


class Company(MetaModel):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    short_text = models.CharField(max_length=500, blank=True, null=True)
    logo = models.ImageField(upload_to="brand", blank=True, null=True)
    show = models.BooleanField(default=False)
    site_url = models.URLField(null=True, blank=True)
    vacancy_url = models.URLField(null=True, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True)
    office = models.ManyToManyField(City)
    show_on_main = models.BooleanField(default=False)
    has_parser = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)
    extra = models.TextField(null=True, blank=True)


class Vacancy(MetaModel):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    short_text = models.CharField(max_length=500, blank=True, null=True)
    date_of_publication = models.DateField(blank=True, null=True)
    show = models.BooleanField(default=False)
    show_on_main = models.BooleanField(default=False)
    vacancy_url = models.URLField(null=True, blank=True)
    company = models.ForeignKey(Company)
    city = models.ForeignKey(City, null=True, blank=True)
    programming_language = models.ForeignKey(ProgrammingLanguage, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    extra = models.TextField(null=True, blank=True)


class UsefullLink(MetaModel):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=False)
    show_on_main = models.BooleanField(default=False)
    url = models.URLField(null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    extra = models.TextField(null=True, blank=True)

