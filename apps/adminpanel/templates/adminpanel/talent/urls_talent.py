# adminpanel/talent/urls.py

from django.urls import path
from apps.adminpanel import views


urlpatterns_talento = [
    path('talento/', views.talentos, name='talento'),
    path('talento/crear/', views.talent_create, name='talent_create'),
    path('talento/<int:id>/eliminar/', views.eliminar_talento, name='talent_delete'),
    path('talents/<int:pk>/json/', views.talent_detail_json, name='talent_detail_json'),
]
