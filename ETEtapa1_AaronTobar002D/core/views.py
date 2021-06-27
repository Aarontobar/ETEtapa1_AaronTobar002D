from django.shortcuts import render
from .models import *

# Create your views here.

def inicio(request):
    productos= producto.objects.all()
    context={'productos': productos}
    return render(request, 'inicio.html', context)

def proveedo(request):
    proveedores= proveedor.objects.all()
    context={'proveedores':proveedores}
    return render(request, 'proveedores.html', context)