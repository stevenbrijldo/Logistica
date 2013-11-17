from django.conf.urls import patterns, url
from carga_trabajo import views

urlpatterns = patterns('',
	

    
	
    #urls de proveedor

      url(r'^proyecto/', 'carga_trabajo.views.proyecto'),
<<<<<<< HEAD
      url(r'^actividad/','carga_trabajo.views.actividad',name='actividad'),
       url(r'^tarea/','carga_trabajo.views.tarea',name='tarea'),
=======
      url(r'^actividad/','carga_trabajo.views.actividad'),
>>>>>>> db87f77ad16adccea928aa77f2c17f3cb1aa2431

    #url(r'^(?P<codigo_proveedor>\d+)/$', views.detalle, name="detalleProveedor"),
)