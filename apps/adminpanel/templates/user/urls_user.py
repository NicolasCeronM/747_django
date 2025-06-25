from django.urls import path
from apps.adminpanel import views


urlpatterns_user = [
    path('user/', views.user_list, name='user_list'),
]
