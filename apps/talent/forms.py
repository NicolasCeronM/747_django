from django import forms
from .models import Talent, TalentSocialLink

class TalentForm(forms.ModelForm):
    class Meta:
        model = Talent
        fields = [
            'full_name', 'brand_name', 'location', 'specialty',
            'biography', 'contact_email', 'phone_number',
            'profile_image', 'cover_image', 'video_url', 'is_verified'
        ]
        labels = {
            'full_name': 'Nombre Completo',
            'brand_name': 'Nombre de Marca/Estudio',
            'location': 'Ubicación',
            'specialty': 'Especialidad',
            'experience': 'Años de Experiencia',
            'biography': 'Biografía',
            'contact_email': 'Email de Contacto',
            'phone_number': 'Número de Teléfono',
            'profile_image': 'Imagen de Perfil',
            'cover_image': 'Imagen de Portada',
            'video_url': 'URL del Video de Presentación',
            'is_verified': 'Marcar como talento verificado',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Ej: María González Silva'}),
            'brand_name': forms.TextInput(attrs={'placeholder': 'Ej: MG Creative Studio'}),
            'location': forms.TextInput(attrs={'placeholder': 'Ej: Santiago, Chile'}),
            'specialty': forms.TextInput(attrs={'placeholder': 'Seleccionar especialidad'}),
            'experience': forms.NumberInput(attrs={'placeholder': 'Ej: 5'}),
            'biography': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe la trayectoria, logros, estilo y experiencia del talento...'}),
            'contact_email': forms.EmailInput(attrs={'placeholder': 'maria@ejemplo.com'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+56 9 1234 5678'}),
            'video_url': forms.URLInput(attrs={'placeholder': 'https://youtube.com/watch?...'}),
        }

class TalentSocialLinkForm(forms.ModelForm):
    class Meta:
        model = TalentSocialLink
        fields = ['platform', 'url']
