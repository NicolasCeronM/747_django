from django.shortcuts import render, get_object_or_404
from .models import Drop
from apps.designer.models import DesignerProfile
from apps.drop.models import Drop
from apps.product.models import Product

# Create your views here.

def drops(request):

    drops = Drop.objects.all()
    designers = DesignerProfile.objects.all()

    data = {
        'drops': drops,
        'designers':designers

    }

    return render(request,'drops.html', data)

def drop_detail(request,id):

    drop = get_object_or_404(Drop,id=id)
    products = Product.objects.filter(drop_id=id)

    
    data = {
        'drop': drop,
        'products':products
    }

    return render(request,'drop_details.html',data)

