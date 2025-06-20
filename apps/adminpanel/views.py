from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'adminpanel/dashboard.html')

def productos(request):
    return render(request, 'adminpanel/producto.html')