from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from apps.user.models import CustomUser
from apps.product.models import Product
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import CartItem, Product
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('cart:view_cart')


@login_required
def view_cart(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart.html', {'cart': cart})

@login_required
def remove_item(request, id):
    item = get_object_or_404(CartItem, id=id, cart__user=request.user)
    item.delete()
    return redirect('cart:view_cart')


#AJAX


@login_required
def cart_count_ajax(request):
    cart = getattr(request.user, 'cart', None)
    count = cart.items.count() if cart else 0
    return JsonResponse({'count': count})

@require_POST
@login_required
def add_to_cart_ajax(request):
    print("POST recibido:", request.POST)
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity', 1))

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        print("Producto no encontrado")
        return JsonResponse({'error': 'Producto no encontrado'}, status=404)

    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()
    print("Producto agregado correctamente")

    return JsonResponse({
        'success': True,
        'cart_count': cart.items.count(),
        'item_quantity': cart_item.quantity,
    })