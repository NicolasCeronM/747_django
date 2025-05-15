from django.shortcuts import render
from .models import Drop
from apps.designer.models import DesignerProfile

# Create your views here.

def drops(request):

    drops = Drop.objects.all()
    designers = DesignerProfile.objects.all()

    data = {
        'drops': drops,
        'designers':designers

    }

    return render(request,'drops.html', data)
