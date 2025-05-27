from django.shortcuts import render
from .models import Product

# Create your views here.

def products(request):

    products = Product.objects.all()

    data = {
        'products' : products
    }

    return render(request,'product.html', data)