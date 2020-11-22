from django.db import models
from django.contrib import admin

#creacion de las clases
class Administrador(models.Model):
    id_admin = models.SmallIntegerField(serialize=True, primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    cedula = models.BigIntegerField()
    telefono = models.BigIntegerField()
    correo = models.CharField(max_length=200)

class Cliente(models.Model):
    id_cliente = models.IntegerField(serialize=True, primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    cedula = models.BigIntegerField()
    fecha_nacimiento = models.DateField()
    telefono = models.BigIntegerField()
    correo = models.CharField(max_length=200)
    clave = models.CharField(max_length=100)

class Direccion(models.Model):
    id_direccion = models.IntegerField(serialize=True, primary_key=True)
    barrio = models.CharField(max_length=45)
    via_principal = models.CharField(max_length=10)
    num_1 = models.SmallIntegerField()
    aux_1 = models.CharField(max_length=5)
    num_2 = models.SmallIntegerField()
    aux_2 = models.CharField(max_length=5)
    num_3 = models.SmallIntegerField()
    inmueble = models.CharField(max_length=45)
    interior = models.CharField(max_length=5)
    num_4 = models.SmallIntegerField()
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Carrito(models.Model):
    id_carrito = models.SmallIntegerField(serialize=True, primary_key=True)
    valor_total = models.SmallIntegerField()
    ic_cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)

class Categoria(models.Model):
    id_categoria = models.SmallIntegerField(serialize=True, primary_key=True)
    nombre = models.CharField(max_length=45)

class Producto(models.Model):
    id_producto = models.SmallIntegerField(serialize=True, primary_key=True)
    nombre = models.CharField(max_length=45)
    precio = models.BigIntegerField()
    tamano = models.IntegerField()
    unidades_disponibles = models.IntegerField()
    id_admin = models.ForeignKey(Administrador, on_delete= models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete= models.CASCADE)

class Carrito_producto(models.Model):
    id_carrito_producto = models.SmallIntegerField(serialize=True, primary_key=True)
    cantidad = models.IntegerField()
    id_producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    id_carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)

class Domiciliario(models.Model):
    id_domiciliario = models.IntegerField(serialize=True, primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    cedula = models.BigIntegerField()
    telefono = models.BigIntegerField()

class Factura(models.Model):
    id_factura = models.SmallIntegerField(serialize=True, primary_key=True)
    fecha = models.DateField()
    valor_total = models.BigIntegerField()
    estado = models.CharField(max_length=45)
    id_domiciliario = models.ForeignKey(Domiciliario, on_delete=models.CASCADE)

class Producto_factura(models.Model):
    id_producto_factura = models.SmallIntegerField(serialize=True, primary_key=True)
    cantidad = models.IntegerField()
    id_producto = models.ForeignKey(Producto, on_delete= models.CASCADE)
    id_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)

#importacion a la pagina de administrador
admin.site.register(Administrador)
admin.site.register(Cliente)
admin.site.register(Direccion)
admin.site.register(Carrito)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Carrito_producto)
admin.site.register(Domiciliario)
admin.site.register(Factura)
admin.site.register(Producto_factura)
  
