# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from solicitud.models import Solicitud
from django.core import serializers
import json
from django.core.paginator import Paginator

def solicitud(request):
	solicitud=Solicitud.objects.all()
	return render_to_response('solicitud.html',{'cont':3,'solicitudes':solicitud}, context_instance=RequestContext(request))
def holaMundo(request):
     html = "<html><body>Hola Mundo desde DJANGO</body></html>"
     return HttpResponse(html)
def agregarSolicitud(request):
	if request.method == 'POST':
		
		cliente = request.POST['cliente']
		descripcion = request.POST['descripcion']
		estado = request.POST['estado']
		fecha = request.POST['fecha']
		solicitud = Solicitud.objects.create(cliente=cliente,descripcion=descripcion,estado=estado,fecha=fecha)
		#Actividad.objects.create(codigo_proyecto=0 ,nombre=descripcion,costo=0,encargado=encargado,fecha_inicio=fecha_inicio,
		#fecha_fin_estimada=fecha_fin_estimada,fecha_fin_real=fecha_fin_real,tipo_actividad=tipo_actividad,estado=estado)
		solicitud=Solicitud.objects.all()
		return render_to_response('solicitud.html',{'cont':3,'solicitudes':Solicitud.objects.all()}, context_instance=RequestContext(request))
	else:
		solicitud=Solicitud.objects.all()
		return render_to_response('solicitud.html',{'cont':3,'solicitudes':solicitud}, context_instance=RequestContext(request))

def modificarSolicitud(request):
	if request.method == 'POST':
		codigo = request.POST['codigo']
		cliente = request.POST['cliente']
		descripcion = request.POST['descripcion']
		estado = request.POST['estado']
		fecha = request.POST['fecha']
		solicitud = Solicitud.objects.get(codigo=codigo)
		solicitud.cliente=cliente
		solicitud.descripcion=descripcion
		solicitud.estado=estado
		solicitud.fecha=fecha
		solicitud.save()
		solicitud=Solicitud.objects.all()
		return render_to_response('solicitud.html',{'cont':3,'solicitudes':Solicitud.objects.all()}, context_instance=RequestContext(request))
	else:
		solicitud=Solicitud.objects.all()
		return render_to_response('solicitud.html',{'cont':3,'solicitudes':solicitud}, context_instance=RequestContext(request))
def buscarSolicitud(request):
	if request.is_ajax():
		if request.method == "POST":
			descripcion = request.POST['descripcion']
			solicitud = Solicitud.objects.filter(descripcion__icontains=descripcion)
			data=serializers.serialize("json",solicitud)
			return HttpResponse(data,mimetype="application/json")
	else:
		solicitud=Solicitud.objects.all()
		return render_to_response('solicitud.html',{'cont':3,'solicitudes':solicitud}, context_instance=RequestContext(request))
def obtenerSolicitud(request):
	if request.is_ajax():
		solicitud = Solicitud.objects.all()
		if(request.method=="POST"):
			pag=request.POST['pag']
			lista=Paginator(solicitud,10)
			cont=lista.num_pages;
			print pag+" sasdf"
			solicitud=lista.page(1).object_list
			if int(pag)>cont:
				solicitud=lista.page(cont).object_list
				pag=cont
			else:
				solicitud=lista.page(int(pag)).object_list	
			data={}
			data['pagina']=pag
			data['informacion']=serializers.serialize("json",solicitud)	
			return HttpResponse(json.dumps(data),mimetype="application/json")
		else:		
			data=serializers.serialize("json",solicitud)
			
			return HttpResponse(data,mimetype="application/json")
	else:
		solicitud=Solicitud.objects.all()
		return render_to_response('solicitud.html',{'cont':3,'solicitudes':solicitud}, context_instance=RequestContext(request))
