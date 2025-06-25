# adminpanel/drop/urls.py

from django.urls import path
from apps.adminpanel import views


urlpatterns_drop = [
    path('drop/', views.drop_list, name='drop_list'),
]
