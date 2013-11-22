# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from mensajes.models import Mensaje
from django.core import serializers
import json
from django.core.paginator import Paginator

def holaMundo(request):
     html = "<html><body>Hola Mundo desde DJANGO</body></html>"
     return HttpResponse(html)
def modificarMensaje(request):
     html = "<html><body>Hola Mundo desde DJANGO</body></html>"
     return HttpResponse(html)
def mensajes(request):   
	return render_to_response('mensajes.html',{'cont':3}, context_instance=RequestContext(request))