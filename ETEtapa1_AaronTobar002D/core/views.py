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

def modproveedor(request):
    return render(request, 'modproveedor.html')

def llamar(request):
    id= request.POST.get("id")
    try:
        proveedores= proveedor.objects.get(numero= id)
        datos= {'form': proveedorform(instance=proveedores)} 
        return render(request, 'core/form_modproveedor.html', {'datos':datos,'proveedores':proveedores})
    except proveedor.DoesNotExist:
        return redirect('modproveedor')
   

def modificar(request, id):
    proveedores= proveedor.objects.get(numero= id)
    if request.method=='POST':  
        formulario= proveedorform(data=request.POST, instance=proveedores)
        if formulario.is_valid():
            formulario.save()
            return redirect('proveedor')
    return redirect('llamar')

def contrasenna(request):

    id= request.POST.get("numero")
    nombre= request.POST.get("p_nombre")
    pais_id= request.POST.get("pais")

    nompais= pais.objects.get(numero=pais_id)
    pais_n= nompais.nombre
    
    id = str(id)[:2]
    nombre= str(nombre.upper())[:2]
    paisn= pais_n[-2:]
    contraseña = id + nombre
    
    post = request.POST.copy()
    post['cantrasenna'] = id + nombre + paisn

    request.POST = post
    form = proveedorform(post, files=request.FILES)
    if form.is_valid():
            form.save()
            return redirect('proveedor')
    else:
        return redirect('formproveedor')

