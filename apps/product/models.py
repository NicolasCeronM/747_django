from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    iamge = models.ImageField(upload_to="product/",null=True,blank=True)
    price = models.IntegerField()
    detail = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, related_name='category')

    def __str__(self):
        return self.name
    
class ProductImage(models.Model):
    image = models.ImageField(upload_to='product/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=1, related_name='iamges')