#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
<<<<<<< HEAD
=======
class Solicitud(models.Model):
	codigo = models.IntegerField(primary_key=True)
	cliente = models.IntegerField()
	descripcion = models.CharField(max_length=100)
	estado =models.CharField(max_length=100)
	fecha = models.DateField(null=False)
	def __unicode__(self):
		return self.nombre
>>>>>>> 000c2dff42fb7a3918687620a8ad2e97406f0deb
