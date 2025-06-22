from django.contrib import admin
from .models import Product, ProductImage, ProductSize

# Register your models here.

class ImageProductAdmin(admin.TabularInline):
    model = ProductImage


class SizeProductAdmin(admin.TabularInline):
    model = ProductSize

class ProductoAdmin(admin.ModelAdmin):
    inlines = [
        ImageProductAdmin,
        SizeProductAdmin
    ]

admin.site.register(Product, ProductoAdmin)


