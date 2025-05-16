from django.db import models
from apps.drop.models import Drop

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    detail = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='products')
    drop = models.ForeignKey(Drop, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
