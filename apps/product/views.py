from django.shortcuts import render
from .models import Product, ProductCategory

# Create your views here.

def products(request):

    products = Product.objects.all()
    categories = ProductCategory.objects.all()

    data = {
        'products' : products,
        'categories':categories
    }

    return render(request,'product.html', data)