from django.contrib import admin
from .models import proveedor, pais, moneda, producto

# Register your models here.

admin.site.register(proveedor)
admin.site.register(pais)
admin.site.register(moneda)
admin.site.register(producto)