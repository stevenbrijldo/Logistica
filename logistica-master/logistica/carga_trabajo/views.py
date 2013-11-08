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
		actividad = Actividad.objects.create(codigo=codigo,nombre=nombre_actividad,costo=costo,encargado=encargado,fecha_inicio=fecha_inicio,
		fecha_fin_estimada=fecha_fin_estimada,fecha_fin_real=fecha_fin_real,tipo_actividad=tipo_actividad)
		actividad=Actividad.objects.all()
		return render_to_response('lista_actividad.html',{'actividades':actividades}, context_instance=RequestContext(request))
	else:
		actividad=Actividad.objects.all()
		return render_to_response('lista_actividad.html',{'actividades':actividades}, context_instance=RequestContext(request))

def actividad(request):
	return render_to_response ('lista_actividad.html',{'cont':3}, context_instance=RequestContext(request))


def indexCompras(request):
	listaCompras = Compra.objects.all()
	context = {'listaCompras':listaCompras}
	return render(request, 'carga_trabajo/index.html', context)

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
		nombre = request.POST['nombre']
		direccion = request.POST['direccion']
		telefono = request.POST['telefono']
		estado = True
		proveedor = Proveedor(codigo,nombre,direccion,telefono,estado)
		proveedor.save()
		return redirect('carga_trabajo.views.indexProveedor')
	else:
		return render(request, 'proveedor/agregar.html')

def editarProveedor(request, codigo_proveedor):
	if request.method == 'POST':
		prov = get_object_or_404(Proveedor, pk=codigo_proveedor)
		if len(request.POST['nuevaDireccion']) > 0:
			prov.direccion = request.POST['nuevaDireccion']
		if request.POST['estado'] == "true":
			prov.estado = True
		else:
			prov.estado = False
		prov.save()
		return redirect('carga_trabajo.views.indexProveedor')
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
		listaProductos = Producto.objects.all()
		return render(request, 'proveedor/agregar_Producto.html', {'listaProductos':listaProductos})