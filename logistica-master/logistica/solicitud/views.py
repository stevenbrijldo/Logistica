# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from solicitud.models import Solicitud
from django.core import serializers

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
	if request.isajax():
		solicitud=Solicitud.objects.all()
		descripcion = request.POST['descripcion']
		solicitud=solicitud.filter(descripcion__icontains=descripcion)
		data=serializers.serialize("json",solicitud)
		return HttpResponse(data,context_type="aplication/json")
	else:
		solicitud=Solicitud.objects.all()
		return render_to_response('solicitud.html',{'cont':3,'solicitudes':solicitud}, context_instance=RequestContext(request))
