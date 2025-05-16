from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    image = models.ImageField('Imagen de perfil', upload_to='perfil/', blank=True, null=True)
    active_user = models.BooleanField(default=True)
    admin_user = models.BooleanField(default=False)

    # ✅ Define is_staff como campo y sincronízalo con admin_user
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username} ({self.email})'

