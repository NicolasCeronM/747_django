# suscripciones/urls.py
from django.urls import path
from . import views

app_name = 'suscripciones'

urlpatterns = [
    path('registrar/', views.guardar_correo, name='guardar_correo'),
]
