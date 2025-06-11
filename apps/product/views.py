from django.shortcuts import render, get_object_or_404
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

def product_detail(request,id ):

    product = get_object_or_404(Product, id=id)

    data = {
        'product':product
    }

    return render(request,'product_detail.html',data)