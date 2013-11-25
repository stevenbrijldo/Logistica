from django.conf.urls import patterns, include, url



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'financiero.views.home', name='home'),
    # url(r'^financiero/', include('financiero.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^$', 'main.home'), #URL a la pagina principal del subsitema financiero

    url(r'^logistica/', include('inicio.urls')),
    url(r'^carga_trabajo/', include('carga_trabajo.urls')),
    url(r'^solicitud/', include('solicitud.urls')),
    url(r'^comunicacion/', include('mensajes.urls')),

    url(r'^agregar_solicitud/$','solicitud.views.agregarSolicitud', name='agregar_solicitud'),
    url(r'^modificar_solicitud/$','solicitud.views.modificarSolicitud', name='modificar_solicitud'),
    url(r'^buscar_solicitud/$','solicitud.views.buscarSolicitud', name='buscar_solicitud'),
    url(r'^obtener_solicitud/$','solicitud.views.obtenerSolicitud', name='obtener_solicitud'),

    url(r'^agregar_mensaje/$','mensajes.views.agregarMensaje', name='agregar_mensaje'),
    url(r'^obtener_mensaje/$','mensajes.views.obtenerMensaje', name='obtener_mensaje'),
    url(r'^hola_mundo/$','mensajes.views.holaMundo', name='hola_mundo'),                  


    url(r'^carga_proyecto/$','carga_trabajo.views.agregarProyecto', name='agregar_proyecto'),
    url(r'^modificar_proyecto/$','carga_trabajo.views.modificarProyecto', name='modificar_proyecto'),
    url(r'^buscar_proyecto/$','carga_trabajo.views.buscarProyecto', name='buscar_proyecto'),
    url(r'^proyecto_atrasado/$','carga_trabajo.views.proyectoAtrasados', name='proyecto_atrasado'),

   
    url(r'^carga_actividad/$','carga_trabajo.views.agregarActividad', name='agregar_actividad'),
    url(r'^modificar_actividad/$','carga_trabajo.views.modificarActividad', name='modificar_actividad'),
    url(r'^tareas_resueltas/$','carga_trabajo.views.tareasResueltas', name='tareas_resueltas'),

    url(r'^carga_tarea/$','carga_trabajo.views.agregarTarea', name='agregar_tarea'),
    url(r'^modificar_tarea/$','carga_trabajo.views.modificarTarea', name='modificar_tarea'),

    url(r'^$', 'usuario.views.index'),
    url(r'^config_user$', 'usuario.views.config_user'),
    url(r'^change_password$', 'usuario.views.change_password'),
    url(r'^login$', 'usuario.views.logIn'),
    url(r'^logout$', 'usuario.views.logOut'),
    url(r'^reestablecer_password$', 'usuario.views.forgot_password'),
    url(r'^satisfactorio$', 'usuario.views.success_change'),
    url(r'^validar_usuario$', 'usuario.views.check_user'),
)
