from django.contrib import admin
from django.urls import path

from .views import Index, Detail

urlpatterns = [
    path('', Index, name='Index'),
    path('producto/<int:pk>', Detail, name='Detail_product')
]