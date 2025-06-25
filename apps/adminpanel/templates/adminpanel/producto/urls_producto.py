from django.urls import path, include
from apps.adminpanel import views

urlpatterns_producto = [
    
    path('producto/', views.productos, name='producto'),
    path('producto/crear/', views.product_create, name='product_create'),
    path('producto/<int:id>/eliminar/', views.eliminar_producto, name='product_delete'),
    # HTMX endpoints
    path('producto/table/', views.productos_htmx, name='producto_table'),
]   