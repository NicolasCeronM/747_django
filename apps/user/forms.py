from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Correo electrónico",
        error_messages={
            'required': 'Este campo es obligatorio.',
            'invalid': 'Ingresa un correo válido.'
        },
        widget=forms.EmailInput(attrs={'placeholder': 'ejemplo@correo.com'})
    )

    username = forms.CharField(
        label="Nombre de usuario",
        error_messages={
            'required': 'Este campo es obligatorio.',
            'invalid': 'Nombre de usuario inválido.'
        },
        widget=forms.TextInput(attrs={'placeholder': 'Ingresa tu nombre de usuario'})
    )

    password1 = forms.CharField(
        label="Contraseña",
        error_messages={'required': 'Este campo es obligatorio.'},
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingresa tu contraseña'})
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        error_messages={'required': 'Este campo es obligatorio.'},
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirma tu contraseña'})
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("Este nombre de usuario ya está registrado.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Este correo ya está registrado.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError({
                'password2': ["Las contraseñas no coinciden."]
            })


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        error_messages={
            'required': 'Este campo es obligatorio.',
            'invalid': 'Nombre de usuario inválido.'
        },
        widget=forms.TextInput(attrs={'placeholder': 'Ingresa tu nombre de usuario'})
    )
    password = forms.CharField(
        label="Contraseña",
        error_messages={'required': 'Este campo es obligatorio.'},
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingresa tu contraseña'})
    )
