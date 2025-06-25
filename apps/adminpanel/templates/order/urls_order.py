from django.urls import path
from apps.adminpanel import views


urlpatterns_order = [
    path('pedido/', views.order_list, name='pedido_list'),
]
