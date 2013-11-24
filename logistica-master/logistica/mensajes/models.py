from django.db import models
from django.contrib.auth.models import User 
from publico.models import Persona

class Mensaje(models.Model):
	de=models.ForeignKey(Persona,related_name='de')
	para=models.ForeignKey(Persona,related_name='para')
	mensaje=models.CharField(max_length=200)
	asunto=models.CharField(max_length=200)
	fecha=models.DateField(null=False)
	def __unicode__(self):
		return self.mensaje