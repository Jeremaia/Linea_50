from django.shortcuts import render, redirect
from firebase_admin import firestore
from .models import Carrito, ItemCarrito, Producto

def agregar_al_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
    item, creado = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    # Aquí puedes realizar cualquier otra lógica que necesites, como incrementar la cantidad del producto en el carrito
    return redirect('ver_carrito')

def ver_carrito(request):
    carrito = Carrito.objects.get(usuario=request.user)

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
