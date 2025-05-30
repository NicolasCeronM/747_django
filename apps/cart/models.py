from django.db import models
from apps.product.models import Product
from apps.user.models import CustomUser

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def total(self):
        return sum(item.subtotal() for item in self.items.all())

    def __str__(self):
        return f'Carro de {self.user.username}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
