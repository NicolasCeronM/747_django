from django.shortcuts import render
from django.contrib import messages
from apps.drop.models import Drop

# Create your views here.

def custom_404(request, exception):
    return render(request, '404.html', status=404)

def home(request):

    latest_drops = Drop.objects.filter(is_active=True).order_by('-created_at')[:3]
    data = {
        'latest_drops':latest_drops
    }
    messages.success(request, "🎉 Felicitaciones, bienvenido a nuestra tienda!")

    return render(request,'index.html', data)

from django.shortcuts import render






