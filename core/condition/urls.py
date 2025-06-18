from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core.condition.views import *

app_name = 'condition'

urlpatterns = [
    path('add/', ConditionCreateView.as_view(), name='create_condition'),
    path('update/<uuid:pk>/', ConditionUpdateView.as_view(), name='update_condition'),
    path('list/', ConditionListView.as_view(), name='list_condition'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
