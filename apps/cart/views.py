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


@require_POST
def add_to_cart_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({'success': False, 'message': 'Debes iniciar sesión.'}, status=403)

    try:
        product_id = request.POST.get('product_id')
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity', 1))

        if not product_id or product_id == 'undefined':
            return JsonResponse({'success': False, 'message': 'ID de producto inválido.'}, status=400)

        product = Product.objects.get(id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)

        filters = {'cart': cart, 'product': product}
        if size:
            filters['size'] = size

        item, created = CartItem.objects.get_or_create(**filters)
        if created:
            item.quantity = quantity
        else:
            item.quantity += quantity
        item.save()

        total_items = CartItem.objects.filter(cart=cart).count()

        return JsonResponse({'success': True, 'message': 'Producto agregado al carrito.', 'total_items': total_items})

    except Product.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Producto no encontrado.'}, status=404)

    except Exception as e:
        import traceback
        
        return JsonResponse({'success': False, 'message': f'Error inesperado: {str(e)}'}, status=500)