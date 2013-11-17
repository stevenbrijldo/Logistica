# Create your views here.
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse
from carga_trabajo.models import Proveedor, Actividad, Proyecto
from atencion.models import Producto
from django.shortcuts import render_to_response
from django.template import RequestContext

#Vistas de Compras

def proyecto(request):
	return render_to_response ('lista_proyectos.html',{'cont':3}, context_instance=RequestContext(request))
def agregarProyecto(request):
	if request.method == 'POST':
		codigo = request.POST['codigo']
		nombre_proyecto = request.POST['nombre']
		encargado = request.POST['encargado']
		objetivo = request.POST['objetivo']
		costo = request.POST['costo']
		fecha_inicio = request.POST['fecha_inicio']
		fecha_fin_estimada = request.POST['fecha_fin_estimada']
		fecha_fin_real = request.POST['fecha_fin_real']
	 	estado= request.POST['estado']
		proyecto = Proyecto.objects.create(codigo=codigo,nombre=nombre_proyecto,costo=costo,encargado=encargado,fecha_inicio=fecha_inicio,
		fecha_fin_estimada=fecha_fin_estimada,fecha_fin_real=fecha_fin_real,objetivo=objetivo,estado=estado)
		proyectos=Proyecto.objects.all()
		return render_to_response('lista_proyectos.html',{'proyectos':proyectos}, context_instance=RequestContext(request))
	else:
		proyectos=Proyecto.objects.all()
		return render_to_response('lista_proyectos.html',{'proyectos':proyectos}, context_instance=RequestContext(request))

def agregarActividad(request):
	if request.method == 'POST':
		codigo = request.POST['codigo']
		nombre_actividad = request.POST['nombre']
		encargado = request.POST['encargado']
		costo = request.POST['costo']
		fecha_inicio = request.POST['fecha_inicio']
		fecha_fin_estimada = request.POST['fecha_fin_estimada']
		fecha_fin_real = request.POST['fecha_fin_real']
	 	tipo_actividad= request.POST['tipo_actividad']
	 	estado= request.POST['estado']
	 	ids=request.POST['ID']
	 	
	 	proyecto=Proyecto.objects.get(codigo=ids) 
		actividad = Actividad.objects.create(codigo_proyecto=proyecto ,codigo=codigo,nombre=nombre_actividad,costo=costo,encargado=encargado,fecha_inicio=fecha_inicio,
		fecha_fin_estimada=fecha_fin_estimada,fecha_fin_real=fecha_fin_real,tipo_actividad=tipo_actividad,estado=estado)
		actividad=Actividad.objects.all()
		return render_to_response('lista_actividad.html',{'actividades':actividades}, context_instance=RequestContext(request))
	else:
		actividad=Actividad.objects.all()
		return render_to_response('lista_actividad.html',{'actividades':actividades}, context_instance=RequestContext(request))

def actividad(request):
<<<<<<< HEAD
	actividadproyecto = request.GET['ID']
	actividad=Actividad.objects.filter(codigo_proyecto=actividadproyecto)
	return render_to_response ('lista_actividad.html',{'cont':3,'proyecto':actividadproyecto}, context_instance=RequestContext(request))

def tarea(request):
	tareaproyecto = request.GET['ID']
	tarea=Tarea.objects.filter(codigo_actividad=tareaproyecto)
	return render_to_response ('lista_tarea.html',{'cont':1,'id':tareaproyecto}, context_instance=RequestContext(request))

def agregarTarea(request):
	if request.method == 'POST':
		codigo = request.POST['codigo']
		nombre_tarea = request.POST['nombre']
		descripcion = request.POST['descripcion']
		fecha_inicio = request.POST['fecha_inicio']
		fecha_fin_estimada = request.POST['fecha_fin_estimada']
		fecha_fin_real = request.POST['fecha_fin_real']
	 	estado_tarea= request.POST['estado_tarea']
	 	ids=request.POST['ID']
	 	actividad=Actividad.objects.get(codigo_actividad=ids)



		tarea = Tarea.objects.create(codigo_actividad=actividad,codigo=codigo,nombre=nombre_tarea,descripcion=descripcion,fecha_inicio=fecha_inicio,
		fecha_fin_estimada=fecha_fin_estimada,fecha_fin_real=fecha_fin_real,estado_tarea=estado_tarea)
		tarea=Tarea.objects.all()
		return render_to_response('lista_tarea.html',{'tarea':tarea}, context_instance=RequestContext(request))
	else:
		tarea=Tarea.objects.all()
		return render_to_response('lista_tarea.html',{'tarea':tarea}, context_instance=RequestContext(request))
=======
	return render_to_response ('lista_actividad.html',{'cont':3}, context_instance=RequestContext(request))


def indexCompras(request):
	listaCompras = Compra.objects.all()
	context = {'listaCompras':listaCompras}
	return render(request, 'carga_trabajo/index.html', context)
>>>>>>> db87f77ad16adccea928aa77f2c17f3cb1aa2431

def agregarCompra(request):
	return HttpResponse("Shedman")

#Vistas de proveedor
def indexProveedor(request):
    listaProveedores = Proveedor.objects.all()
    context = {'listaProveedores': listaProveedores}
    return render(request, 'proveedor/index.html', context)

def agregarProveedor(request):
	if request.method == 'POST':
		codigo = request.POST['codigo']
<<<<<<< HEAD
		nombre_proyecto = request.POST['nombre']
		encargado = request.POST['encargado']
		objetivo = request.POST['objetivo']
		costo = request.POST['costo']
		fecha_inicio = request.POST['fecha_inicio']
		fecha_fin_estimada = request.POST['fecha_fin_estimada']
		fecha_fin_real = request.POST['fecha_fin_real']
	 	estado= request.POST['estado']
		proyecto = Proyecto.objects.get(pk=codigo)
		proyecto.nombre=nombre_proyecto
		proyecto.encargado=encargado
		proyecto.objetivo=objetivo
		proyecto.costo=costo
		proyecto.fecha_fin_real=fecha_fin_real
		proyecto.estado=estado
		proyecto.save()
		proyectos=Proyecto.objects.all()
		return render_to_response('lista_proyectos.html',{'proyectos':proyectos}, context_instance=RequestContext(request))
=======
		nombre = request.POST['nombre']
		direccion = request.POST['direccion']
		telefono = request.POST['telefono']
		estado = True
		proveedor = Proveedor(codigo,nombre,direccion,telefono,estado)
		proveedor.save()
		return redirect('carga_trabajo.views.indexProveedor')
>>>>>>> db87f77ad16adccea928aa77f2c17f3cb1aa2431
	else:
		return render(request, 'proveedor/agregar.html')

def editarProveedor(request, codigo_proveedor):
	if request.method == 'POST':
<<<<<<< HEAD
		codigo = request.POST['codigo']
		nombre_actividad = request.POST['nombre']
		encargado = request.POST['encargado']
		costo = request.POST['costo']
		fecha_inicio = request.POST['fecha_inicio']
		fecha_fin_estimada = request.POST['fecha_fin_estimada']
		fecha_fin_real = request.POST['fecha_fin_real']
	 	tipo_actividad= request.POST['tipo_actividad']
	 	estado= request.POST['estado']
	 	actividad = Actividad.objects.get(pk=codigo)
		actividad.nombre=nombre_actividad
		actividad.encargado=encargado
		actividad.costo=costo
		actividad.fecha_fin_real=fecha_fin_real
		actividad.estado=estado
		actividad.save()
		actividad=Actividad.objects.all()
		return render_to_response('lista_actividad.html',{'actividad':actividad}, context_instance=RequestContext(request))
=======
		prov = get_object_or_404(Proveedor, pk=codigo_proveedor)
		if len(request.POST['nuevaDireccion']) > 0:
			prov.direccion = request.POST['nuevaDireccion']
		if request.POST['estado'] == "true":
			prov.estado = True
		else:
			prov.estado = False
		prov.save()
		return redirect('carga_trabajo.views.indexProveedor')
>>>>>>> db87f77ad16adccea928aa77f2c17f3cb1aa2431
	else:
		return render(request, 'proveedor/index.html')

def listaProductosProveedor(request, codigo_proveedor):
	listaAuxiliar = Producto_Proveedor.objects.filter(proveedor = codigo_proveedor)
	#listaProductos = get_list_or_404(Producto, pk=listaAuxiliar__producto)
	proveedor = get_object_or_404(Proveedor, pk=codigo_proveedor)
	return render(request, 'proveedor/detalle.html', {'listaAuxiliar':listaAuxiliar,'proveedor':proveedor})

def agregarProductoProveedor(request, codigo_proveedor):
	if request.method == 'POST':
		HttpResponse("Formulario Enviado")
	else:
<<<<<<< HEAD
		tarea=Tarea.objects.all()
	return render_to_response('lista_tarea.html',{'tarea':tarea}, context_instance=RequestContext(request))

def desactivarProyecto(request):
	if request.method == 'POST':
		codigo = request.POST['codigo']
		nombre_proyecto = request.POST['nombre']
		encargado = request.POST['encargado']
		objetivo = request.POST['objetivo']
		costo = request.POST['costo']
		fecha_inicio = request.POST['fecha_inicio']
		fecha_fin_estimada = request.POST['fecha_fin_estimada']
		fecha_fin_real = request.POST['fecha_fin_real']
	 	estado= request.POST['estado']
		proyecto = Proyecto.objects.get(pk=codigo)
		proyecto.estado=estado
		return render_to_response('lista_proyectos.html',{'proyectos':proyectos}, context_instance=RequestContext(request))
	else:
		proyectos=Proyecto.objects.all()
	return render_to_response('lista_proyectos.html',{'proyectos':proyectos}, context_instance=RequestContext(request))
	

def desactivarActividad(request):
	if request.method == 'POST':
		codigo = request.POST['codigo']
		nombre_actividad = request.POST['nombre']
		encargado = request.POST['encargado']
		costo = request.POST['costo']
		fecha_inicio = request.POST['fecha_inicio']
		fecha_fin_estimada = request.POST['fecha_fin_estimada']
		fecha_fin_real = request.POST['fecha_fin_real']
	 	tipo_actividad= request.POST['tipo_actividad']
	 	estado= request.POST['estado']
		actividad = Actividad.objects.get(pk=codigo)
		actividad.estado=estado
		actividad.save()
		actividad=Actividad.objects.all()
		return render_to_response('lista_actividad.html',{'actividad':actividad}, context_instance=RequestContext(request))
	else:
		actividad=Actividad.objects.all()
	return render_to_response('lista_actividad.html',{'actividad':actividad}, context_instance=RequestContext(request))
	
=======
		listaProductos = Producto.objects.all()
		return render(request, 'proveedor/agregar_Producto.html', {'listaProductos':listaProductos})
>>>>>>> db87f77ad16adccea928aa77f2c17f3cb1aa2431
