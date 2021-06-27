from django.db import models

# Create your models here.

class pais(models.Model):
    numero= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')
    nombre= models.CharField(max_length=100, verbose_name='nombre')

    def __str__(self):
        return self.nombre

class moneda(models.Model):
    numero= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')
    nombre= models.CharField(max_length=100, verbose_name='nombre')

    def __str__(self):
        return self.nombre

class proveedor(models.Model):
    numero= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')
    imagen= models.ImageField(verbose_name='foto')
    p_nombre= models.CharField(max_length=50, verbose_name='p_nombre')
    s_nombre= models.CharField(max_length=50, verbose_name='s_nombre')
    ap_paterno= models.CharField(max_length=50, verbose_name='ap_paterno')
    ap_materno= models.CharField(max_length=50, verbose_name='ap_materno')
    telefono= models.IntegerField(verbose_name='telefono')
    direccion= models.CharField(max_length=400, verbose_name='direccion')
    email= models.CharField(max_length=200, verbose_name='email')
    pais= models.ForeignKey(pais, on_delete=models.CASCADE)
    cantrasenna= models.CharField(max_length=100, verbose_name='contrasenna')
    moneda= models.ForeignKey(moneda, on_delete=models.CASCADE)

    @property
    def imagenURL(self):
        try:
            url= self.imagen.url
        except:
            url=''
        return url

    def __str__(self):
        return self.p_nombre




class producto(models.Model):
    numero= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')
    proveedor= models.ForeignKey(proveedor, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=100, verbose_name='nombre')
    imagen= models.ImageField(verbose_name='imagen')
    descripcion= models.CharField(max_length=500, verbose_name='descripcion')

    @property
    def imagenURL(self):
        try:
            url= self.imagen.url
        except:
            url=''
        return url

    def __str__(self):
        return self.nombre