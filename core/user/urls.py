from django.urls import path
from core.user.views import *

app_name = 'user'

urlpatterns = [
    path('add/', UserCreateView.as_view(), name='user_create'),
    path('list/', UserListView.as_view(), name='user_list'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('profile/<int:pk>/', MyProfileDetailView.as_view(), name='user_profile'),
    # path('edit/password/', UserChangePasswordView.as_view(), name='change_password'),
    # path('register/', registerview, name='account_create')
]