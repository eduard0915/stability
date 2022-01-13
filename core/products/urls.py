from django.conf.urls.static import static
from django.urls import path

from config import settings
from core.products.views import *

app_name = 'products'

urlpatterns = [
    path('add/', ProductCreateView.as_view(), name='product_create'),
    path('list/', ProductListView.as_view(), name='product_list'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
