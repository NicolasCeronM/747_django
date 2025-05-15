from django.shortcuts import render
from .models import DesignerProfile

# Create your views here.

def designers(request):

    designers = DesignerProfile.objects.all()

    data = {
        'designers' :designers
    }

    return render(request,'designers.html', data)
