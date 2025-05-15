from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class Usuario(AbstractBaseUser):
    username = models.CharField('Nombre de usuario', unique=True, max_length=100)
    email = models.EmailField('Correo electronico', max_length=254, unique=True)
    names = models.CharField('Nombres', max_length=200, blank=True, null=True)
    last_names = models.CharField('Apellidos', max_length=200, blank=True, null=True)
    image = models.ImageField('Imagenn de perfil',upload_to='perfil/', height_field=None, width_field=None, max_length=200)
    active_user = models.BooleanField(default=True)
    admin_user = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = 'email','names','last_names'

    def __str__(self):
        return f'{self.names}, {self.last_names}'
    
    def has_perm(self.perm,obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.admin_user