from django.contrib import admin

from .models import Negocio, Categoria, Producto, publicacion

# Register your models here.

@admin.register(Negocio)
class NegocioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'whatsapp', 'email', 'create_at', 'updated']

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['categoria', 'create_at', 'updated']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'categoria', 'disponible', 'create_at', 'updated']
    list_filter = ['categoria', 'disponible',]

@admin.register(publicacion)
class publicacionAdmin(admin.ModelAdmin):
    list_display = ['create_at',]
    list_filter = ['create_at',]