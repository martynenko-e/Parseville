from django.contrib import admin
from .models import *

class AdminCity(admin.ModelAdmin):
    list_display = ('name', 'alias', 'show')
    list_editable = ('show',)

class AdminCountry(admin.ModelAdmin):
    list_display = ('name', 'alias', 'show')
    list_editable = ('show',)

class AdminProgram(admin.ModelAdmin):
    list_display = ('name', 'alias', 'show')
    list_editable = ('show',)

class AdminLink(admin.ModelAdmin):
    list_display = ('name', 'alias', 'show', 'url', 'added_date')
    list_editable = ('show',)

class AdminCompany(admin.ModelAdmin):
    list_display = ('name', 'alias', 'show', 'country', 'site_url', 'has_logo', 'extra', 'added_date')
    list_editable = ('show',)

    def has_logo(self, obj):
        return obj.logo != ""

    has_logo.boolean = True

class AdminVacancy(admin.ModelAdmin):
    list_display = ('name', 'alias', 'show', 'company', 'extra')
    list_editable = ('show',)

admin.site.register(Country, AdminCountry)
admin.site.register(City, AdminCity)
admin.site.register(UsefullLink, AdminLink)
admin.site.register(Company, AdminCompany)
admin.site.register(Vacancy, AdminVacancy)
admin.site.register(ProgrammingLanguage, AdminProgram)
