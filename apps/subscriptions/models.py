from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)
    accepted_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.email