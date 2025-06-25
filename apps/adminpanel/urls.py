# adminpanel/urls.py
from django.urls import path
from . import views
from  apps.adminpanel.templates.adminpanel.producto import urls_producto
from  apps.adminpanel.templates.adminpanel.talent import urls_talent
from  apps.adminpanel.templates.drop import urls_drop
from  apps.adminpanel.templates.order import urls_order
from  apps.adminpanel.templates.user import urls_user

app_name = 'adminpanel'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
]+ urls_producto.urlpatterns_producto + urls_talent.urlpatterns_talento + urls_drop.urlpatterns_drop + urls_order.urlpatterns_order + urls_user.urlpatterns_user