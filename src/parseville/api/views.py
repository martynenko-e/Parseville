from rest_framework import permissions
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
)
from parseville.models import (
    Vacancy,
    Company,
    )
from .serializers import (
    CompanySerializer,
    VacancySerializer,
    )

from rest_framework import viewsets


# class VacancyListAPIView(ListAPIView):
#     queryset = Vacancy.objects.all()
#     serializer_class = VacancyListSerializer


# class CompanyListAPIView(ListAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanyListSerializer


# class CompanyDetailAPIView(RetrieveAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanyDetailSerializer
#     lookup_field = 'pk'

# class VacancyDetailAPIView(RetrieveAPIView):
#     queryset = Vacancy.objects.all()
#     serializer_class = VacancyDetailSerializer
#     lookup_field = 'pk'


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer



class VacancyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer