from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.create_order, name='create'),
    path('success/<int:order_id>/', views.order_success, name='success'),
    path('invoice/<int:order_id>/download/', views.download_invoice, name='download_invoice'),
]