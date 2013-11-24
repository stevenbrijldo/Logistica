# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import password_reset
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.models import User
from django.utils import simplejson
import uuid

@login_required
def change_password(request):
	actual_user = request.user
	if request.POST.get('new_pass') == request.POST.get('repeat_pass'):
		actual_user.set_password(request.POST.get('new_pass'))
		actual_user.save()
		data = simplejson.dumps({
			'html': u"""<p>Su contraseña fue cambiada satisfactoriamente.</p>""",
			'status': 'success'
		})
		return HttpResponse(data, mimetype="application/json")
	else:
		data = simplejson.dumps({
			'html': u"""<p>Sus contraseñas no son iguales.</p>""",
			'status': 'error'
		})
		return HttpResponse(data, mimetype="application/json")

def check_user(request):
	user = request.POST.get('user',False)
	if User.objects.filter(username=user).count() == 0:
		data = simplejson.dumps({
			'html': '<p>El usuario no existe.</p>',
		})
		return HttpResponse(data, mimetype='application/json')
	else:
		password = str(uuid.uuid4())
		actual_user = User.objects.filter(username=user)[0]
		actual_user.set_password(password)
		actual_user.save()
		actual_user.email_user('Nueva Contraseña',
		 u""" El presente email es enviado en respuesta a su peticion de olvido de contraseña.

		 Contraseña nueva:"""+password+u""" 

		 Ya puede iniciar sesion en el sistema con su nueva contraseña.""")
		mail = actual_user.email
		data = simplejson.dumps({
			'url': '/',
			'html': u"""<p>Su nueva contraseña fue enviada al correo """+mail+""".</p>""",
		})
		return HttpResponse(data, mimetype='application/json')

def config_user(request):
	return render_to_response('config_user.html', context_instance=RequestContext(request))

def forgot_password(request):
	return render_to_response('reestablecer_password.html', context_instance=RequestContext(request))

def index(request):
	if request.user.is_active:
		return render_to_response('rh_base.html', {'user': request.user}, context_instance=RequestContext(request))
	else:
		return render_to_response('login.html', {'user': request.user}, context_instance=RequestContext(request))

def logIn(request):
	user = request.POST['user']
	password = request.POST['password']
	logeduser = authenticate(username=user, password=password)
	
	if logeduser is not None:
		if logeduser.is_active:
			login(request, logeduser)
			data = simplejson.dumps({'url': '/',})
			return HttpResponse(data, mimetype='application/json')
		else:
			data = simplejson.dumps({'html': '<p>El usuario no esta activo.</p>',})
			return HttpResponse(data, mimetype='application/json')
	else:
		data = simplejson.dumps({'html': u"""<p>La combinacion usuario contraseña es incorrecta.</p>""",})
		return HttpResponse(data, mimetype='application/json')

def logOut(request):
	logout(request)
	return redirect('/')

def success_change(request):
	return render_to_response('cambio_satisfactorio.html')
