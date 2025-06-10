from apps.orders.models import Order, OrderItem
from apps.product.models import Product
from apps.cart.models import Cart


def create_order_from_cart(request, payment_id=None):
    try:
        cart = Cart.objects.get(user=request.user)
    except Cart.DoesNotExist:
        return None

    cart_items = cart.items.all()
    if not cart_items:
        return None

    total = sum(item.product.price * item.quantity for item in cart_items)

    order = Order.objects.create(
        user=request.user,
        total=total,
        payment_id=payment_id,
        status='Pagado'
    )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            subtotal=item.product.price * item.quantity
        )

    # Vaciar el carrito
    cart.items.all().delete()

    return order