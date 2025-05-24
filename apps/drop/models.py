from django.db import models
from apps.designer.models import DesignerProfile

class Drop(models.Model):
    name = models.CharField(max_length=100)
    drop_number = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    designers = models.ManyToManyField(DesignerProfile, related_name='drops')
    launch_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    cover_image = models.ImageField(upload_to='drops/cover/')
    hero_video = models.URLField(blank=True,null=True, help_text="URL del video documental o presentación")
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    social_impact = models.TextField(help_text="Cómo este drop apoya a la comunidad")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.launch_date.year})"

    class Meta:
        ordering = ['-launch_date']
