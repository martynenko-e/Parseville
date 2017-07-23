from .views import (
    CompanyViewSet,
    VacancyViewSet,
)

company_list = CompanyViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

company_detail = CompanyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

vacancy_list = VacancyViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

vacancy_detail = VacancyViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


# urlpatterns = [
#     url(r'^vacancy/$', VacancyListAPIView.as_view(), name='vacancy_list'),
#     url(r'^vacancy/(?P<pk>\d+)/$', VacancyDetailAPIView.as_view(), name='vacancy_detail'),
#     url(r'^company/$', CompanyListAPIView.as_view(), name='company_list'),
#     url(r'^company/(?P<pk>\d+)/$', CompanyDetailAPIView.as_view(), name='company_detail'),
#     # url(r'^create', PointCreateAPIView.as_view(), name='create'),
#     # # url(r'^(?P<slug>[\w-]+)/$', PointDetailAPIView.as_view(), name='detail'),
#     # url(r'^(?P<pk>[\w-]+)/edit/$', PointUpdateAPIView.as_view(), name='update'),
#     # url(r'^(?P<pk>[\w-]+)/delete/$', PointDeleteAPIView.as_view(), name='delete'),
# ]