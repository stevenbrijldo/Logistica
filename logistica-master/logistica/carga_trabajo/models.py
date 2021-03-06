from django.db import models
from solicitud.models import Solicitud


# Create your models here.
class Proyecto(models.Model):
	codigo = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=100)
	encargado = models.CharField(max_length=100)
	fecha_inicio = models.DateField(null=False)
	fecha_fin_estimada = models.DateField(null=False)
	fecha_fin_real = models.DateField(null=False)
	objetivo = models.CharField(max_length=100)
	estado = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Actividad(models.Model):
	codigo = models.AutoField(primary_key=True)
	codigo_proyecto=models.ForeignKey(Proyecto,null=True)
	codigo_solicitud=models.ForeignKey(Solicitud,null=True)
	nombre = models.CharField(max_length=100)
	encargado = models.CharField(max_length=100)
	fecha_inicio = models.DateField(null=False)
	fecha_fin_estimada = models.DateField(null=False)
	fecha_fin_real = models.DateField(null=False)
	tipo_actividad = models.CharField(max_length=100)
	estado = models.CharField(max_length=100)
	def __unicode__(self):
		return self.nombre

class Tarea(models.Model):
	codigo = models.AutoField(primary_key=True)
	codigo_actividad=models.ForeignKey(Actividad)
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=100)
	fecha_inicio = models.DateField(null=False)
	fecha_fin_estimada = models.DateField(null=False)
	fecha_fin_real = models.DateField(null=False)
	estado_tarea = models.CharField(max_length=100)
	def __unicode__(self):
		return self.nombre