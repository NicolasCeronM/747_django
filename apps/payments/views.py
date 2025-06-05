# Django imports
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

# Modelos y lógica propia
from apps.cart.models import Cart
from apps.orders.utils import create_order_from_cart
from .utils import enviar_correo_compra, generar_factura_pdf

# Mercado Pago
from .services.mercado_pago import crear_preferencia

# WebPay
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.options import WebpayOptions

# ====================================================
# ✅ VISTAS DE CHECKOUT Y PAGO CON MERCADO PAGO
# ====================================================

def checkout(request):
    """
    Genera la preferencia de pago con Mercado Pago y muestra el resumen del carrito.
    """
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()

    if not cart_items:
        return redirect("cart:view_cart")

    resumen_items = []
    for item in cart_items:
        resumen_items.append({
            "title": item.product.name,
            "quantity": item.quantity,
            "unit_price": float(item.product.price),
            "subtotal": float(item.product.price * item.quantity),
        })

    total = sum(i["subtotal"] for i in resumen_items)

    # Guardar resumen en sesión
    request.session["payment_summary"] = {
        "items": resumen_items,
        "total": total
    }

    # Crear preferencia de Mercado Pago
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
        "success": "https://2kvhrc1g-8000.brs.devtunnels.ms/payments/checkout/success/",
        "failure": "https://2kvhrc1g-8000.brs.devtunnels.ms/payments/failure/",
        "pending": "https://2kvhrc1g-8000.brs.devtunnels.ms/payments/pending/"
    }

    preference = crear_preferencia(productos, back_urls)

    return render(request, "checkout.html", {
        "cart_items": cart_items,
        "total": total,
        "preference_id": preference["id"],
        "public_key": settings.MP_PUBLIC_KEY
    })


def checkout_success(request):
    """
    Procesa el retorno de Mercado Pago después del pago. Crea la orden si fue aprobado.
    """
    payment_status = request.GET.get('status')
    payment_id = request.GET.get('payment_id')

    if payment_status == 'approved':
        order = create_order_from_cart(request, payment_id=payment_id)
        return redirect('orders:success', order_id=order.id)
    else:
        return render(request, 'failed.html')


def failure(request):
    return render(request, 'mercado_pago/failure.html')


def pending(request):
    return render(request, 'mercado_pago/pending.html')


# ====================================================
# ✅ VISTAS DE WEBPAY
# ====================================================

def webpay_init(request):
    """
    Inicia una transacción con Webpay.
    """
    cart = Cart.objects.get(user=request.user)
    cart_items = cart.items.all()

    total = sum(item.product.price * item.quantity for item in cart_items)

    buy_order = f"order-{request.user.id}-{cart.id}"
    session_id = f"session-{request.user.id}"
    return_url = request.build_absolute_uri("/payments/webpay/return/")

    tx = Transaction(WebpayOptions(
        commerce_code="597055555532",
        api_key="579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C",
        integration_type="TEST"
    ))

    response = tx.create(buy_order, session_id, total, return_url)

    return redirect(response["url"] + "?token_ws=" + response["token"])


def webpay_return(request):
    token = request.GET.get("token_ws")

    if not token:
        return render(request, 'failed.html')

    tx = Transaction(WebpayOptions(
        commerce_code="597055555532",  
        api_key="579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C",
        integration_type="TEST"
    ))

    response = tx.commit(token)

    if response.get("status") == "AUTHORIZED":
        order = create_order_from_cart(
            request,
            payment_id=response.get("payment_response", {}).get("payment_code", "")  # o usa 'buy_order'
        )
        if order:
            enviar_correo_compra(request.user, order)
            return redirect('orders:success', order_id=order.id)
        else:
            return render(request, 'failed.html', {'message': 'No se pudo crear la orden. Carrito vacío o no encontrado.'})





# ====================================================
# ✅ VISTA GENÉRICA (opcional si usas sesión solamente)
# ====================================================

def payment_success(request):
    """
    Vista de confirmación genérica (si se usa sesión en vez de orden real).
    Ya no es necesaria si se usa `orders:success` correctamente.
    """
    order = request.session.get("payment_summary")

    context = {
        "payment_id": request.GET.get("payment_id"),
        "status": request.GET.get("status", "approved"),
        "payment_type": request.GET.get("payment_type", "unknown"),
        "order": order
    }

    # Limpieza del carrito
    try:
        cart = Cart.objects.get(user=request.user)
        cart.items.all().delete()
    except:
        pass

    request.session.pop("payment_summary", None)

    return render(request, "success.html", context)
