from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from .models import Order, OrderItem
from apps.product.models import Product
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q

@login_required
def create_order(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('cart:view_cart')  # ajusta según tu URL

    total = sum(item['price'] * item['quantity'] for item in cart.values())
    order = Order.objects.create(user=request.user, total=total)

    for product_id, item in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item['quantity'],
                subtotal=item['price'] * item['quantity']
            )
        except Product.DoesNotExist:
            continue

    # Limpiar carrito
    request.session['cart'] = {}

    return redirect('orders:success', order_id=order.id)

def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    order_items = order.items.all()  # ajusta según tus relaciones
    return render(request, 'orders/success.html', {
        'order': order,
        'order_items': order_items
    })

def download_invoice(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    template_path = 'orders/invoice_pdf.html'
    context = {'order': order}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="factura_orden_{order.id}.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF', status=500)
    return response

# MIS PEDIDOS

@login_required
def mis_pedidos(request):
    orders = Order.objects.filter(user=request.user).select_related('user').prefetch_related('items__product')
    
    estado = request.GET.get('estado')
    fecha = request.GET.get('fecha')
    query = request.GET.get('q')

    if estado:
        orders = orders.filter(status__iexact=estado)

    if fecha:
        days = int(fecha)
        from_date = timezone.now() - timedelta(days=days)
        orders = orders.filter(created_at__gte=from_date)

    if query:
        orders = orders.filter(
            Q(id__icontains=query) |
            Q(items__product__name__icontains=query)
        ).distinct()

    orders = orders.order_by('-created_at')

    return render(request, 'orders/mis_pedidos.html', {'orders': orders})