# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from mensajes.models import Mensaje
from publico.models import Persona
from django.core import serializers
import json
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from datetime import*

def holaMundo(request):
	html = "<html><body>Hola Mundo desde DJANGO</body></html>"
	return HttpResponse(html)

def modificarMensaje(request):
	html = "<html><body>Hola Mundo desde DJANGO</body></html>"
	return HttpResponse(html)

def mensajes(request): 
	persona=Persona.objects.all()  
	return render_to_response('mensajes.html',{'cont':3,'personas':persona}, context_instance=RequestContext(request))
@login_required(login_url='/')
def agregarMensaje(request):
	if request.method=="POST":
		mensaje=request.POST['mensaje']
		asunto=request.POST['asunto']
		de=Persona.objects.get(documento=request.user.username)
		para=Persona.objects.get(documento=request.POST['para'])
		Mensaje.objects.create(mensaje=mensaje,de=de,para=para,fecha=datetime.today(),asunto=asunto)
		persona=Persona.objects.all() 
		return render_to_response('mensajes.html',{'mensajes':Mensaje.objects.all(),'personas':persona}, context_instance=RequestContext(request))
	else:
		return render_to_response('mensajes.html',{'mensajes':Mensaje.objects.all()}, context_instance=RequestContext(request))	
def obtenerMensaje(request):
	if request.is_ajax():
		mensaje = Mensaje.objects.filter(para=Persona.objects.get(documento=request.user.username))
		if(request.method=="POST"):
			pag=request.POST['pag']
			lista=Paginator(mensaje,10)
			cont=lista.num_pages;
			print pag+" sasdf"
			mensaje=lista.page(1).object_list
			if int(pag)>cont:
				mensaje=lista.page(cont).object_list
				pag=cont
			else:
				mensaje=lista.page(int(pag)).object_list	
			data={}
			data['pagina']=pag
			data['informacion']=serializers.serialize("json",mensaje)	
			return HttpResponse(json.dumps(data),mimetype="application/json")
		else:		
			data=serializers.serialize("json",mensaje)
			return HttpResponse(data,mimetype="application/json")
	else:
		mensaje=Mensaje.objects.all()
		return render_to_response('mensajes.html',{'cont':3,'mensajes':mensaje}, context_instance=RequestContext(request))	


		