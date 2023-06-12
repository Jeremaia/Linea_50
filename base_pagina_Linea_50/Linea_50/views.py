from django.shortcuts import render, redirect
from google.cloud import firestore

# Ejemplo de vistas
"""
class YourView(request):
    return render(request, 'yourappname/yourtemplate.html')
"""

# TODO: Cambiar el como funciona esta vista cuando se crea la base de datos con tal de que lea los datos

def home(request):
    """
    db = firestore.Client()
    collection_ref = db.collection('Tipo-producto')
    docs = collection_ref.stream()

    data = []
    for doc in docs:
        data.append(doc.to_dict())

    print(data)
    """
    return render(request, 'home.html') #, {'data': data})