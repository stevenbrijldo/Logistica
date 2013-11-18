# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from datetime import *

def solicitud(request):
	return render_to_response ('solicitud.html',{'cont':3}, context_instance=RequestContext(request))
