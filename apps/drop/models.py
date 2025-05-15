from django.db import models
from apps.designer.models import DesignerProfile

# Create your models here.

class Drop(models.Model):
    name = models.CharField(max_length=100)
    designers = models.ManyToManyField(DesignerProfile, related_name='drops')
    launch_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    theme = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='drops/cover/')
    hero_video = models.FileField(upload_to='drops/videos/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    social_impact = models.TextField(help_text="How this drop supports the community")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.launch_date.year})"

    class Meta:
        ordering = ['-launch_date']