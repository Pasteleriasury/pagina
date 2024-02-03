from django.contrib import admin

from .models import Metrica

# Register your models here.

@admin.register(Metrica)
class MetricaAdmin(admin.ModelAdmin):
    list_display = ['create_at',]
    list_filter = ['create_at',]
