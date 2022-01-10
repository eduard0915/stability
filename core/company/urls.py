from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core.company.views import CompanyCreateView, CompanyUpdateView, CompanyListView


app_name = 'company'

urlpatterns = [
    path('add/', CompanyCreateView.as_view(), name='company_create'),
    path('update/<int:pk>/', CompanyUpdateView.as_view(), name='company_update'),
    path('list/', CompanyListView.as_view(), name='company_list'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)