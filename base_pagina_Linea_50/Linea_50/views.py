from django.shortcuts import render, redirect

# Ejemplo de vistas
"""
class YourView(request):
    return render(request, 'yourappname/yourtemplate.html')
"""

# TODO: Cambiar el como funciona esta vista cuando se crea la base de datos con tal de que lea los datos

def home(request):
    return render(request, 'home.html')