# Django imports
from django.shortcuts import render, redirect
from django.contrib import messages
# Own imports
from django.conf import settings
from apps.cart.models import CartItem, Cart
# Mercado pago imports
from .services.mercado_pago import crear_preferencia
# WebPay imports
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.options import WebpayOptions

# Create your views here.

# MERCADO PAGO VIEWS

def checkout(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()

    if not cart_items:
        return redirect("cart:view_cart" )

    resumen_items = []
    for item in cart_items:
        resumen_items.append({
            "title": item.product.name,
            "quantity": item.quantity,
            "unit_price": float(item.product.price),
            "subtotal": float(item.product.price * item.quantity),
            #"image": item.product.image.url if item.product.image else None
        })

    total = sum(i["subtotal"] for i in resumen_items)

    request.session["payment_summary"] = {
        "items": resumen_items,
        "total": total
    }

    # 🟦 Crear preferencia Mercado Pago
    productos = [
        {
            "title": item["title"],
            "quantity": item["quantity"],
            "unit_price": item["unit_price"],
            "currency_id": "CLP"
        }
        for item in resumen_items
    ]

    back_urls = {
        "success": "https://2kvhrc1g-8000.brs.devtunnels.ms//payments/success/",
        "failure": "https://2kvhrc1g-8000.brs.devtunnels.ms//payments/failure/",
        "pending": "https://2kvhrc1g-8000.brs.devtunnels.ms//payments/pending/"
    }

    preference = crear_preferencia(productos, back_urls)
    #print("MP preference response:", preference)


    return render(request, "checkout.html", {
        "cart_items": cart_items,
        "total": total,
        "preference_id": preference["id"],
        "public_key": settings.MP_PUBLIC_KEY
    })

def success(request):
    context = {
        "collection_id": request.GET.get("collection_id"),
        "collection_status": request.GET.get("collection_status"),
        "payment_id": request.GET.get("payment_id"),
        "status": request.GET.get("status"),
        "payment_type": request.GET.get("payment_type"),
        "merchant_order_id": request.GET.get("merchant_order_id"),
    }

    return render(request, "success.html", context)

def failure(request):
    return render(request, "mercado_pago/failure.html")

def pending(request):
    return render(request, "mercado_pago/pending.html")

# webPay VIEWS

def webpay_init(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()

    total = sum(item.product.price * item.quantity for item in cart_items)

    buy_order = f"order-{request.user.id}-{cart.id}"
    session_id = f"session-{request.user.id}"
    return_url = request.build_absolute_uri("/payments/success/")

    tx = Transaction(WebpayOptions(
        commerce_code="597055555532",
        api_key="579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C",
        integration_type="TEST"
    ))

    response = tx.create(buy_order, session_id, total, return_url)

    return redirect(response["url"] + "?token_ws=" + response["token"])


def webpay_commit(request):
    token = request.GET.get("token_ws")

    tx = Transaction(WebpayOptions(
        commerce_code="597055555532",  
        api_key="579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C",
        integration_type="TEST"
    ))

    response = tx.commit(token)

    order = request.session.pop("webpay_order", None)

    return render(request, "success.html", {
        "response": response,
        "order": order
    })


# VIEWS COMPARTIDAS

def payment_success(request):
    order = request.session.get("payment_summary")

    context = {
        "payment_id": request.GET.get("payment_id"),
        "status": request.GET.get("status", "approved"),
        "payment_type": request.GET.get("payment_type", "unknown"),
        "order": order
    }

    # Limpia carrito del usuario
    try:
        cart = Cart.objects.get(user=request.user)
        cart.items.all().delete()
    except:
        pass

    # Limpia resumen de sesión
    request.session.pop("payment_summary", None)

    return render(request, "success.html", context)




