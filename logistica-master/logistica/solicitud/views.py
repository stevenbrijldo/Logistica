# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from solicitud.models import Solicitud

def solicitud(request):
	return render_to_response ('solicitud.html',{'cont':3}, context_instance=RequestContext(request))
def holaMundo(request):
     html = "<html><body>Hola Mundo desde DJANGO</body></html>"
     return HttpResponse(html)
def agregarSolicitud(request):
	if request.method == 'POST':
		codigo = request.POST['codigo']
		cliente = request.POST['cliente']
		descripcion = request.POST['descripcion']
		estado = request.POST['estado']
		fecha = request.POST['fecha']
		solicitud = Solicitud.objects.create(cliente=cliente,codigo=codigo,descripcion=descripcion,estado=estado,fecha=fecha)
		solicitud=Solicitud.objects.all()
		return render_to_response('solicitud.html',{'cont':3}, context_instance=RequestContext(request))
	else:
		solicitud=Solicitud.objects.all()
		return render_to_response('solicitud.html',{'cont':3}, context_instance=RequestContext(request))
