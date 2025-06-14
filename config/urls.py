"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls'),name='home'),
    path('designer/', include('apps.designer.urls'), name='designer'),
    path('drops/', include('apps.drop.urls'), name='drops'),
    path('user/', include('apps.user.urls'), name='user'),
    path('product/', include('apps.product.urls'), name='product'),
    path('cart/', include('apps.cart.urls'), name='cart'),
    path('payments/', include('apps.payments.urls'), name='payments'),
    path('orders/', include('apps.orders.urls'), name='orders'),



    path('logout/', LogoutView.as_view(), name='logout'),
]

handler404 = 'apps.home.views.custom_404'


urlpatterns += [
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root':settings.MEDIA_ROOT,
    })
]
