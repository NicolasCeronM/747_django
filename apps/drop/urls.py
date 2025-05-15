from django.urls import path
from . import views

app_name = 'drop'

urlpatterns = [
    path('', views.home, name='home' )
]