# adminpanel/urls.py
from django.urls import path
from . import views

app_name = 'adminpanel'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('producto/', views.productos, name='producto'),
    path('producto/crear/', views.product_create, name='product_create'),
    path('producto/<int:id>/eliminar/', views.eliminar_producto, name='product_delete'),


    # HTMX endpoints
    path('producto/table/', views.productos_htmx, name='producto_table'),
]