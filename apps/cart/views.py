from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from apps.product.models import Product
from django.contrib.auth.decorators import login_required

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