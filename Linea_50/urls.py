from django.shortcuts import render
from django.urls import path
from . import views

# Ejemplo de urls
"""
app_name = 'yourappname' # En caso de existir multiples apps en el proyecto, de no ser asi ignorar

#
urlpatterns = [
    path('', views.HomeView, name='home'),
    path('about/', views.AboutView, name='about'),
    path('contact/', views.ContactView, name='contact'),
]
"""

# TODO: Ingresar Urls de la aplicacion

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('ver/', views.ver_carrito, name='ver_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
]