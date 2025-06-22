from django.db import models

class Talent(models.Model):
    full_name = models.CharField(max_length=100)
    brand_name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    biography = models.TextField()

    # Contacto
    contact_email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    # Multimedia
    profile_image = models.ImageField(upload_to='talents/profile/')
    cover_image = models.ImageField(upload_to='talents/cover/', blank=True)
    video_url = models.URLField(blank=True, help_text="Video de presentación/documental")
    

    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def featured_in_list(self):
        return self.featured_in.split('\n') if self.featured_in else []

    def __str__(self):
        return f"{self.full_name} - {self.brand_name or 'Independiente'}"

    class Meta:
        ordering = ['-is_verified', '-created_at']
        

class TalentSocialLink(models.Model):
    PLATFORM_CHOICES = [
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
        ('website', 'Website'),
        ('facebook', 'Facebook'),
        ('youtube', 'YouTube'),
        ('tiktok', 'TikTok'),
        ('otro', 'Otro'),
    ]

    talent = models.ForeignKey(Talent, on_delete=models.CASCADE, related_name='social_links')
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()

    def __str__(self):
        return f"{self.get_platform_display()}: {self.url}"
