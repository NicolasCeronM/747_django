from django.db import models
from apps.drop.models import Drop

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='products')
    drop = models.ForeignKey(Drop, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    discount = models.IntegerField( blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_sizes", null=True, blank=True)
    size = models.CharField(max_length=10)  # Ej: S, M, L

    def __str__(self):
        return f"{self.product.name} - {self.size}"

class ProductColor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_colors", null=True, blank=True)
    name = models.CharField(max_length=50)
    hex_code = models.CharField(max_length=7, default="#000000")  # Para mostrar visual

    def __str__(self):
        return f"{self.product.name} - {self.name}"
