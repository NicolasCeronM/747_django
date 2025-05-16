from django.shortcuts import render, get_object_or_404
from .models import DesignerProfile

# Create your views here.

def designers(request):

    designers = DesignerProfile.objects.all()

    data = {
        'designers' :designers
    }

    return render(request,'designers.html', data)

def designer_detail(request,id):

    designer = get_object_or_404(DesignerProfile,id=id)

    data = {
        'designer':designer
    }

    return render(request,'designer_detail.html', data)
