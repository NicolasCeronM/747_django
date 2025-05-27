from django.contrib import admin
from .models import Product, ProductCategory, ProductImage

# Register your models here.

class ImageProductAdmin(admin.TabularInline):
    model = ProductImage

class ProductoAdmin(admin.ModelAdmin):
    inlines = [
        ImageProductAdmin
    ]

admin.site.register(Product, ProductoAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductImage)
