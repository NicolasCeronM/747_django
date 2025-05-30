from django.contrib import admin
from .models import Product, ProductCategory, ProductImage, ProductColor, ProductSize

# Register your models here.

class ImageProductAdmin(admin.TabularInline):
    model = ProductImage

class ColorProductAdmin(admin.TabularInline):
    model = ProductColor

class SizeProductAdmin(admin.TabularInline):
    model = ProductSize

class ProductoAdmin(admin.ModelAdmin):
    inlines = [
        ImageProductAdmin,
        ColorProductAdmin,
        SizeProductAdmin
    ]

admin.site.register(Product, ProductoAdmin)
admin.site.register(ProductCategory)


