from django.db import models
from apps.user.models import CustomUser

class DesignerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='designer_profile')
    brand_name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    years_experience = models.PositiveIntegerField(default=1)
    biography = models.TextField()
    profile_image = models.ImageField(upload_to='designers/profile/')
    cover_image = models.ImageField(upload_to='designers/cover/')
    video_url = models.URLField(blank=True, help_text="URL del video destacado")
    featured_in = models.TextField(blank=True, help_text="Publicaciones o medios destacados (uno por línea)")
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def featured_in_list(self):
        return self.featured_in.split('\n') if self.featured_in else []

    def __str__(self):
        return f"{self.user.username} - {self.brand_name or 'Independiente'}"

    class Meta:
        ordering = ['-is_verified', '-created_at']
