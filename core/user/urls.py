from django.conf.urls.static import static
from django.urls import path

from config import settings
from core.user.views import *

app_name = 'user'

urlpatterns = [
    path('add/', UserCreateView.as_view(), name='user_create'),
    path('list/', UserListView.as_view(), name='user_list'),
    path('update/<uuid:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('update-password/<uuid:pk>/', UserPasswordUpdateView.as_view(), name='user_password_update'),
    path('detail/<uuid:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('profile/<uuid:pk>/', MyProfileDetailView.as_view(), name='user_profile'),
    path('profile/edit/<uuid:pk>/', ProfileUpdateView.as_view(), name='user_profile_update'),
    path('edit/password/', UserChangePasswordView.as_view(), name='change_password'),
    # path('register/', registerview, name='account_create')
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
