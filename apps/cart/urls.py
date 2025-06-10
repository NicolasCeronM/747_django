from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:id>/', views.remove_item, name='remove_item'),
    #Nuevas acciones con ajax
    # path('count/', views.cart_count_ajax, name='cart_count_ajax'),
    # path('add/', views.add_to_cart_ajax, name='add_to_cart_ajax'),

]
