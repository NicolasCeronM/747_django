from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products, name='products' ),
    path('detail/<int:id>',views.product_detail, name='product_detail'),
]