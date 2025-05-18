from django.shortcuts import render, get_object_or_404
from .models import DesignerProfile
from apps.drop.models import Drop

# Create your views here.

def designers(request):

    designers = DesignerProfile.objects.all()

    data = {
        'designers' :designers
    }

    return render(request,'designers.html', data)

def designer_detail(request,id):

    designer = get_object_or_404(DesignerProfile,id=id)
    drop = Drop.objects.filter(is_active=True).order_by('-created_at')[:5]

    data = {
        'designer':designer,
        'drop':drop
    }

    return render(request,'designer_detail.html', data)
