# Create your views here.
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse
from carga_trabajo.models import Actividad, Proyecto, Tarea
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from datetime import *

from django.core import serializers

from solicitud.models import Solicitud


#Vistas de Compras

def proyecto(request):
	return render_to_response ('lista_proyectos.html',{'cont':3}, context_instance=RequestContext(request))
def agregarProyecto(request):
	if request.method == 'POST':		
		nombre_proyecto = request.POST['nombre']
		encargado = request.POST['encargado']
		objetivo = request.POST['objetivo']
		fecha_inicio = request.POST['fecha_inicio']
		fecha_fin_estimada = request.POST['fecha_fin_estimada']
		fecha_fin_real = request.POST['fecha_fin_real']
	 	estado= request.POST['estado']
		proyecto = Proyecto.objects.create(nombre=nombre_proyecto,encargado=encargado,fecha_inicio=fecha_inicio,
		fecha_fin_estimada=fecha_fin_estimada,fecha_fin_real=fecha_fin_real,objetivo=objetivo,estado=estado)
		proyectos=Proyecto.objects.all()
		return render_to_response('lista_proyectos.html',{'proyectos':proyectos}, context_instance=RequestContext(request))
	else:
		proyectos=Proyecto.objects.all()
		return render_to_response('lista_proyectos.html',{'proyectos':proyectos}, context_instance=RequestContext(request))

def agregarActividad(request):
	if request.method == 'POST':
		
		nombre_actividad = request.POST['nombre']
		encargado = request.POST['encargado']
		
		fecha_inicio = request.POST['fecha_inicio']
		fecha_fin_estimada = request.POST['fecha_fin_estimada']
		fecha_fin_real = request.POST['fecha_fin_real']
	 	tipo_actividad= request.POST['tipo_actividad']
	 	estado= request.POST['estado']
	 	ids=request.POST['codigo']
	 	proyecto=Proyecto.objects.get(codigo=ids) 
		actividad = Actividad.objects.create(codigo_proyecto=proyecto ,nombre=nombre_actividad,encargado=encargado,fecha_inicio=fecha_inicio,
		fecha_fin_estimada=fecha_fin_estimada,fecha_fin_real=fecha_fin_real,tipo_actividad=tipo_actividad,estado=estado)
		actividad.save()
		actividad=Actividad.objects.filter(codigo_proyecto=ids)
		return render_to_response('lista_actividad.html',{'actividades':actividad,'proyecto':ids}, context_instance=RequestContext(request))
	else:
		actividad=Actividad.objects.all()
		return render_to_response('lista_actividad.html',{'actividades':actividad}, context_instance=RequestContext(request))

def agregarActividadSolicitud(request):
	if request.method == 'POST':
		
		nombre_actividad = request.POST['nombre']
		encargado = request.POST['encargado']
		
		fecha_inicio = request.POST['fecha_inicio']
		fecha_fin_estimada = request.POST['fecha_fin_estimada']
		fecha_fin_real = request.POST['fecha_fin_real']
	 	tipo_actividad= request.POST['tipo_actividad']
	 	estado= request.POST['estado']
	 	ids=request.POST['codigo']
	 	print request.POST
	 	solicitud=Solicitud.objects.get(codigo=int(ids)) 
		actividad = Actividad.objects.create(codigo_solicitud=solicitud ,nombre=nombre_actividad,encargado=encargado,fecha_inicio=fecha_inicio,
		fecha_fin_estimada=fecha_fin_estimada,fecha_fin_real=fecha_fin_real,tipo_actividad=tipo_actividad,estado=estado)
		actividad.save()
		actividad=Actividad.objects.filter(codigo_solicitud=ids)
		return render_to_response('lista_actividad2.html',{'actividades':actividad,'solicitud':ids}, context_instance=RequestContext(request))
	else:
		actividad=Actividad.objects.all()
		return render_to_response('lista_actividad2.html',{'actividades':actividad}, context_instance=RequestContext(request))

def solicitud(request):
	actividadsolicitud = request.GET['ID']
	actividad=Actividad.objects.filter(codigo_solicitud=actividadsolicitud)
	return render_to_response ('lista_actividad2.html',{'cont':3,'solicitud':actividadsolicitud,'actividades':actividad}, context_instance=RequestContext(request))


def actividad(request):
	actividadproyecto = request.GET['ID']
	actividad=Actividad.objects.filter(codigo_proyecto=actividadproyecto)
	return render_to_response ('lista_actividad.html',{'cont':3,'proyecto':actividadproyecto,'actividades':actividad}, context_instance=RequestContext(request))

def tarea(request):
	tareaproyecto = request.GET['ID']
	tarea=Tarea.objects.filter(codigo_actividad=tareaproyecto)
	return render_to_response ('lista_tarea.html',{'cont':1,'actividad':tareaproyecto,'tarea':tarea}, context_instance=RequestContext(request))

def agregarTarea(request):
	if request.method == 'POST':
		nombre_tarea = request.POST['nombre']
		descripcion = request.POST['descripcion']
		fecha_inicio = request.POST['fecha_inicio']
		fecha_fin_estimada = request.POST['fecha_fin_estimada']
		fecha_fin_real = request.POST['fecha_fin_real']
	 	estado_tarea= request.POST['estado_tarea']
	 	ids=request.POST['codigo']
	 	actividad=Actividad.objects.get(codigo=ids)
		tarea = Tarea.objects.create(codigo_actividad=actividad,nombre=nombre_tarea,descripcion=descripcion,fecha_inicio=fecha_inicio,
		fecha_fin_estimada=fecha_fin_estimada,fecha_fin_real=fecha_fin_real,estado_tarea=estado_tarea)
		tarea=Tarea.objects.filter(codigo_actividad=ids)
		return render_to_response('lista_tarea.html',{'tarea':tarea,'actividad':ids}, context_instance=RequestContext(request))
	else:
		tarea=Tarea.objects.all()
		return render_to_response('lista_tarea.html',{'tarea':tarea}, context_instance=RequestContext(request))		



def modificarProyecto(request):
	if request.method == 'POST':
		codigo = request.POST['codigo']
		nombre_proyecto = request.POST['nombre']
		encargado = request.POST['encargado']
		objetivo = request.POST['objetivo']
		fecha_inicio = request.POST['fecha_inicio']
		fecha_fin_estimada = request.POST['fecha_fin_estimada']
		fecha_fin_real = request.POST['fecha_fin_real']
	 	estado= request.POST['estado']
		proyecto = Proyecto.objects.get(pk=codigo)
		proyecto.nombre=nombre_proyecto
		proyecto.encargado=encargado
		proyecto.objetivo=objetivo
		
		proyecto.fecha_inicio=fecha_inicio
		proyecto.fecha_fin_estimada=fecha_fin_estimada
		proyecto.fecha_fin_real=fecha_fin_real
		proyecto.estado=estado
		proyecto.save()
		proyectos=Proyecto.objects.all()
		return render_to_response('lista_proyectos.html',{'proyectos':proyectos}, context_instance=RequestContext(request))
	else:
		proyectos=Proyecto.objects.all()
	return render_to_response('lista_proyectos.html',{'proyectos':proyectos}, context_instance=RequestContext(request))
	

def modificarActividad(request):
	if request.method == 'POST':
		codigo = request.POST['codigo']
		nombre_actividad = request.POST['nombre']
		encargado = request.POST['encargado']
		fecha_inicio = request.POST['fecha_inicio']
		fecha_fin_estimada = request.POST['fecha_fin_estimada']
		fecha_fin_real = request.POST['fecha_fin_real']
	 	tipo_actividad= request.POST['tipo_actividad']
	 	estado= request.POST['estado']
	 	actividad = Actividad.objects.get(pk=codigo)
		actividad.nombre=nombre_actividad
		actividad.encargado=encargado
		actividad.fecha_inicio=fecha_inicio
		actividad.fecha_fin_estimada=fecha_fin_estimada
		actividad.fecha_fin_real=fecha_fin_real
		actividad.tipo_actividad=tipo_actividad
		actividad.estado=estado
		actividad.save()
		actividad=Actividad.objects.all()
		return render_to_response('lista_actividad.html',{'actividad':actividad}, context_instance=RequestContext(request))
	else:
		actividad=Actividad.objects.all()
	return render_to_response('lista_actividad.html',{'actividad':actividad}, context_instance=RequestContext(request))
	

def modificarTarea(request):
	if request.method == 'POST':
		codigo = request.POST['codigo']
		nombre_tarea = request.POST['nombre']
		descripcion = request.POST['descripcion']
		fecha_inicio = request.POST['fecha_inicio']
		fecha_fin_estimada = request.POST['fecha_fin_estimada']
		fecha_fin_real = request.POST['fecha_fin_real']
	 	estado_tarea = request.POST['estado_tarea']
		tarea = Tarea.objects.get(pk=codigo)
		tarea.nombre=nombre_tarea
		tarea.descripcion=descripcion
		tarea.fecha_inicio=fecha_inicio
		tarea.fecha_fin_estimada=fecha_fin_estimada
		tarea.fecha_fin_real=fecha_fin_real
		tarea.save()
		tarea=Tarea.objects.all()
		return render_to_response('lista_tarea.html',{'tarea':tarea}, context_instance=RequestContext(request))
	else:
		tarea=Tarea.objects.all()
	return render_to_response('lista_tarea.html',{'tarea':tarea}, context_instance=RequestContext(request))

def buscarProyecto(request):
	if request.isajax():
		proyecto=Proyecto.objects.all()
		nombre_proyecto = request.POST['nombre_proyecto']
		proyecto=proyecto.filter(nombre_proyecto__icontains=nombre_proyecto)
		data=serializers.serialize("json",proyecto)
		return HttpResponse(data,context_type="aplication/json")
	else:
		proyecto=Proyecto.objects.all()
		return render_to_response('lista_proyecto.html',{'cont':3,'proyectos':proyecto}, context_instance=RequestContext(request))


def proyectoAtrasados(request):
	proyectos = Proyecto.objects.filter(fecha_fin_estimada__lt=date.today())
	return render_to_response('alertas.html',{'cont':3,'proyectos':proyectos}, context_instance=RequestContext(request))

def tareasResueltas(request):
	tareas = Tarea.objects.filter(estado_tarea="Resuelto")

	return HttpResponse(serializers.serialize("json",tareas),mimetype="aplication/json")	

