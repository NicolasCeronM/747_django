from django.db import models
from apps.talent.models import Talent
# from django.utils.text import slugify Hcerlo cuando se reinicie la BBDD

class Drop(models.Model):
    name = models.CharField(max_length=100)
    drop_number = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,blank=True,verbose_name='slug')
    talent = models.ManyToManyField(Talent, related_name='drops')
    description = models.TextField()
    cover_image = models.ImageField(upload_to='drops/cover/')
    hero_video = models.URLField(blank=True,null=True, help_text="URL del video documental o presentación")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.name} ({self.created_at.year})"

    class Meta:
        ordering = ['-created_at']
