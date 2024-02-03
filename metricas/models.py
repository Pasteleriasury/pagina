from django.db import models

# Create your models here.

class Metrica(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)