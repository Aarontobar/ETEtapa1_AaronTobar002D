from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def inicio(request):
    productos= producto.objects.all()
    context={'productos': productos}
    return render(request, 'inicio.html', context)

def proveedo(request):
    proveedores= proveedor.objects.all()
    context={'proveedores':proveedores}
    return render(request, 'proveedores.html', context)

def eliminar(request):
    return render(request, 'eliminar.html')

def quitar(request):
    id=request.POST.get("id")
    try:
        proveedores= proveedor.objects.get(numero=id)
        proveedores.delete()
        return redirect('proveedor')
    except proveedor.DoesNotExist:
        return redirect('eliminar')

def formproveedor(request):
    
    if request.method=='POST':
        form= proveedorform(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('proveedor')
    else:
        form=proveedorform()
    return render(request, 'core/form_proveedor.html', {'form': form})