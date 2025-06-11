from django.db import models
from apps.product.models import Product
from apps.user.models import CustomUser

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    payment_id = models.CharField(max_length=100, blank=True, null=True)  # para almacenar ID de MercadoPago/Webpay
    status = models.CharField(max_length=50, default='Pendiente')  # puedes usar: Pendiente, Pagado, Cancelado, etc.

    @property
    def subtotal(self):
        return sum(item.subtotal for item in self.items.all())

    def __str__(self):
        return f"Orden #{self.id} - {self.user.username}"
    
    


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def hola(self):
        return('prueba de funcion')

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

