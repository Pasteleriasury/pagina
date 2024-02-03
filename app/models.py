from django.db import models

from ckeditor.fields import RichTextField

# Create your models here.

# Datos del negocio

class Negocio(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=124)
    logo = models.CharField(max_length=224, null=True, blank=True)
    whatsapp = models.CharField(max_length=24)
    email = models.CharField(max_length=124, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    descripcion = RichTextField(blank=True,null=True)
    #descripcion = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = 'Negocio'

# Productos

class Categoria(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=124)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.categoria

class Producto(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    nombre = models.CharField(max_length=124)
    precio = models.FloatField()
    imagen = models.CharField(max_length=264)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
    descripcion = RichTextField(blank=True,null=True)
    #descripcion = models.TextField()
    disponible = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class publicacion(models.Model):
    create_at= models.DateField(auto_now_add=True)
    body = RichTextField()

    def __str__(self):
        return str(self.create_at)
    
    class Meta:
        verbose_name_plural = 'Publicaciones'
