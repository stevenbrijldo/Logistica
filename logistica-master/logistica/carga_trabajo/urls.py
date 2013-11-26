from django.conf.urls import patterns, url
from carga_trabajo import views

urlpatterns = patterns('',
	

    
	
    #urls de proveedor

      url(r'^proyecto/', 'carga_trabajo.views.proyecto'),
      url(r'^actividad/','carga_trabajo.views.actividad',name='actividad'),
      url(r'^solicitud/','carga_trabajo.views.solicitud',name='solicitud'),
       url(r'^tarea/','carga_trabajo.views.tarea',name='tarea'),

    #url(r'^(?P<codigo_proveedor>\d+)/$', views.detalle, name="detalleProveedor"),
)