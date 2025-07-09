from django.contrib.auth.models import User
from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=200)                  # Título
    summary = models.CharField(max_length=300)                # Resumen o descripción corta
    content = models.TextField()                              # Contenido principal
    image = models.ImageField(upload_to='images/')             # Imagen
    date_created = models.DateField(auto_now_add=True)        # Fecha de creación

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f"Perfil: {self.user.username}"

    
# Create your models here.
