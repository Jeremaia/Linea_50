from django.shortcuts import render
from firebase_admin import firestore

# Ejemplo de vistas
"""
class YourView(request):
    return render(request, 'yourappname/yourtemplate.html')
"""

db = firestore.client()

def home(request):
    # Obtener datos de la base de datos
    collection_ref = db.collection('Tipo-producto')

    # Almacenamiento de los datos
    docs = collection_ref.get()

    data = []
    cont = 0
    for doc in docs:
        data.append(doc.to_dict())
        data[cont]['id'] = cont+1
        cont += 1

    return render(request, 'home.html', {'productos': data})