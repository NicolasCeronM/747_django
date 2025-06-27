# user/views.py
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home:home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomLoginForm  # ← aquí se aplica tu formulario personalizado
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home:home')
