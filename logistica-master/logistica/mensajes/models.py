from django.db import models
from django.contrib.auth.models import User 


class Mensaje(models.Model):
	de=models.CharField(max_length=100)
	para=models.CharField(max_length=100)
	mensaje=models.CharField(max_length=200)
	def __unicode__(self):
		return self.mensaje 	

class Persona(models.Model):
    documento=models.BigIntegerField(primary_key=True, null=False)
    nombres= models.CharField(max_length=50, null=False)
    apellidos= models.CharField(max_length=50, null=False)
    direccion= models.CharField(max_length=50, null=False)
    telefono1= models.CharField(max_length=50, null=False)
    telefono2= models.CharField(max_length=50)
    hojaVida= models.FileField(upload_to="docs/")
    estado= models.BooleanField(null=False, default=True)
    def __unicode__ (self):
            return self.nombres+' '+self.apellidos