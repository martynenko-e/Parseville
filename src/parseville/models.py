from django.db import models
import settings

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
    logo = models.ImageField(upload_to="%s/brand/" % settings.MEDIA_ROOT, blank=True, null=True)
    show = models.BooleanField(default=False)
    site_url = models.URLField(null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    office = models.CharField(max_length=500, null=True, blank=True)
    show_on_main = models.BooleanField(default=False)

    @property
    def get_absolute_image_url(self):
        return '%s%s' % (settings.MEDIA_URL, self.logo.url)


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


class UsefullLink(MetaModel):
    name = models.CharField(max_length=200)
    alias = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=False)
    show_on_main = models.BooleanField(default=False)
    url = models.URLField(null=True, blank=True)

