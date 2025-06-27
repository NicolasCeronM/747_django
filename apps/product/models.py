from django.db import models
from apps.drop.models import Drop
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    drop = models.ForeignKey(Drop, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    discount = models.IntegerField( blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image = CloudinaryField('image')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_sizes", null=True, blank=True)
    size = models.CharField(max_length=10)  # Ej: S, M, L

    def __str__(self):
        return f"{self.product.name} - {self.size}"
    


