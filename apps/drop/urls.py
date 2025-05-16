from django.urls import path
from . import views

app_name = 'drop'

urlpatterns = [
    path('', views.drops, name='drops' ),
    path('<int:id>/', views.drop_detail, name='drop_detail' )
]