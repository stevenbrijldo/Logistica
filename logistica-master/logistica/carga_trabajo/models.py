from django.db import models
from atencion.models import Producto

# Create your models here.
class Proyecto(models.Model):
	codigo = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10,decimal_places=2)
	encargado = models.CharField(max_length=100)
	fecha_inicio = models.DateField(null=False)
	fecha_fin_estimada = models.DateField(null=False)
	fecha_fin_real = models.DateField(null=False)
	objetivo = models.CharField(max_length=100)
	estado = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Actividad(models.Model):
	codigo = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=100)
	costo = models.DecimalField(max_digits=10,decimal_places=2)
	encargado = models.CharField(max_length=100)
	fecha_inicio = models.DateField(null=False)
	fecha_fin_estimada = models.DateField(null=False)
	fecha_fin_real = models.DateField(null=False)
	tipo_actividad = models.CharField(max_length=100)
	estado = models.CharField(max_length=100)
	def __unicode__(self):
		return self.nombre

class Proveedor(models.Model):
	codigo = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=100, null=False)
	direccion = models.CharField(max_length=100, null=False)
	telefono = models.CharField(max_length=50, null=False)
	estado = models.BooleanField(null=False)
	def __unicode__(self):
		return self.nombre

class Producto_Proveedor(models.Model):
	precio_oferta = models.BigIntegerField(null=False)
	proveedor = models.ForeignKey(Proveedor, null=False)
	producto = models.ForeignKey(Producto,null=False)
	def __unicode__(self):
		return ' ofrecido por '+self.proveedor__nombre
