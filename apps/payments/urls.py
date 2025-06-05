from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    # Mercado pago
    path("checkout/", views.checkout, name="checkout"),
    path("failure/", views.failure, name="failure"),
    path("pending/", views.pending, name="pending"),

    #WebPay
    path("webpay/", views.webpay_init, name="webpay_init"),
    # path("webpay/commit/", views.webpay_commit, name="webpay_commit"),
    # ------
    path('webpay/return/', views.webpay_return, name='webpay_return'),


    #AMBAS
    path("success/", views.checkout_success, name="payment_success"),


]