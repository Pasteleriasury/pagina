from django.shortcuts import render

from metricas.models import Metrica

from .models import Negocio, Producto, Categoria, publicacion

# Create your views here.

def Index(request):

    metrica = Metrica()

    metrica.save()

    datos_negocio = Negocio.objects.all()
    productos = Producto.objects.filter(disponible=True)
    categorias = Categoria.objects.all()
    posts = publicacion.objects.all()

    for i in range(len(datos_negocio)):
        nombre = datos_negocio[i].nombre
        logo = datos_negocio[i].logo
        whatsapp = datos_negocio[i].whatsapp
        email = datos_negocio[i].email
        direccion = datos_negocio[i].direccion
        descripcion = datos_negocio[i].descripcion

    context = {
        #Datos del negocio
        'nombre': nombre,
        'logo': logo,
        'whatsapp': whatsapp,
        'email': email,
        'descripcion': descripcion,

        #Productos
        'productos':productos,

        #Categorias
        'categorias':categorias,

        'posts': posts,
    }

    if direccion != '':
        context['direccion'] = direccion
    
    #print(context)

    return render(request, 'index.html', context)

def Detail(request, pk):

    datos_negocio = Negocio.objects.all()
    producto_datos = Producto.objects.filter(id=pk)

    for i in range(len(datos_negocio)):
        nombre = datos_negocio[i].nombre
        logo = datos_negocio[i].logo
        whatsapp = datos_negocio[i].whatsapp
        email = datos_negocio[i].email
        direccion = datos_negocio[i].direccion
        descripcion = datos_negocio[i].descripcion

    context = {
        #Datos del negocio
        'nombre': nombre,
        'logo': logo,
        'whatsapp': whatsapp,
        'email': email,
        'direccion': direccion,
        'descripcion': descripcion,

        #Productos
        'producto':producto_datos,
    }

    return render(request, 'detail_product.html', context)
