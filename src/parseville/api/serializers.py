from rest_framework.serializers import (
    ModelSerializer, 
    RelatedField, 
    SerializerMethodField
    )
from parseville.models import (
    Vacancy,
    Company,
    )


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ('name',)


class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('name',)


# class CompanyDetailSerializer(ModelSerializer):
#     vacancies = VacancySerializer(many=True)
#     class Meta:
#         model = Company
#         fields = [
#             'id',
#             'alias',
#             'name',
#             'description',
#             'vacancies'
#         ]


# class CompanyListSerializer(ModelSerializer):
#     logo = SerializerMethodField('get_logo_url')

#     class Meta:
#         model = Company
#         fields = [
#             'id',
#             'name',
#             'date',
#             'short_text',
#             'logo'
#         ]

#     def get_logo_url(self, obj):
#         # return self.context['request'].build_absolute_uri(obj.logo.url)
#         return "%s" % obj.logo.url



# class VacancyDetailSerializer(ModelSerializer):
#     class Meta:
#         model = Vacancy
#         fields = [
#             'id',
#             'alias',
#             'name',
#             'description',
#             ''
#         ]


# class VacancyListSerializer(ModelSerializer):
#     company = CompanySerializer()
#     class Meta:
#         model = Vacancy
#         depth = 1
#         fields = [
#             'id',
#             'name',
#             'date',
#             'company'
#         ]

