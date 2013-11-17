from django.conf.urls import patterns, url
from carga_trabajo import views

urlpatterns = patterns('',
	

    
	
    #urls de proveedor

      url(r'^proyecto/', 'carga_trabajo.views.proyecto'),
      url(r'^actividad/','carga_trabajo.views.actividad'),

    #url(r'^(?P<codigo_proveedor>\d+)/$', views.detalle, name="detalleProveedor"),
)