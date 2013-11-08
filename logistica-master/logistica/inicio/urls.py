from django.conf.urls import patterns, url
from carga_trabajo import views

urlpatterns = patterns('',
    #urls de compras
    
    #urls de proveedor

      url(r'^logistica_inicio/', 'inicio.views.inicio'),
#url(r'^(?P<codigo_proveedor>\d+)/$', views.detalle, name="detalleProveedor"),
)