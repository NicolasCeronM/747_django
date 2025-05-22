from django.db import models
from apps.user.models import CustomUser

class DesignerProfile(models.Model):
    #Usuario
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='talent_profile')
    brand_name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    years_experience = models.PositiveIntegerField(default=1)
    biography = models.TextField()

    #Contacto
    contact_email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    #RRSS
    instagram_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    website_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)

    profile_image = models.ImageField(upload_to='talents/profile/')
    cover_image = models.ImageField(upload_to='talents/cover/')
    video_url = models.URLField(blank=True, help_text="URL del video documental o presentación")
    featured_in = models.TextField(blank=True, help_text="Publicaciones o medios destacados (uno por línea)")

    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def featured_in_list(self):
        return self.featured_in.split('\n') if self.featured_in else []

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.brand_name or 'Independiente'}"

    class Meta:
        ordering = ['-is_verified', '-created_at']