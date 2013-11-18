from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'financiero.views.home', name='home'),
    # url(r'^financiero/', include('financiero.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),

    #url(r'^$', 'main.home'), #URL a la pagina principal del subsitema financiero

    url(r'^logistica/', include('inicio.urls')),
    url(r'^carga_trabajo/', include('carga_trabajo.urls')),
    url(r'^solicitud/', include('solicitud.urls')),

    url(r'^carga_proyecto/$','carga_trabajo.views.agregarProyecto', name='agregar_proyecto'),
    url(r'^modificar_proyecto/$','carga_trabajo.views.modificarProyecto', name='modificar_proyecto'),
   
    url(r'^carga_actividad/$','carga_trabajo.views.agregarActividad', name='agregar_actividad'),
    url(r'^modificar_actividad/$','carga_trabajo.views.modificarActividad', name='modificar_actividad'),

    url(r'^carga_tarea/$','carga_trabajo.views.agregarTarea', name='agregar_tarea'),
    url(r'^modificar_tarea/$','carga_trabajo.views.modificarTarea', name='modificar_tarea'),
)