from django.conf.urls import url, include
from . import views


urlpatterns = [
	#url(r'^$', views.mostrar_inicio),
	url(r'^$', views.mostrar_inicio, name='index'), 
    url(r'^index/$', views.mostrar_inicio, name='index'),
    url(r'^galeria/$', views.mostrar_galeria, name='galeria'),
    url(r'^quienessomos/$', views.mostrar_quienessomos, name='quienessomos'),
    url(r'^productos/$', views.mostrar_Productos, name='productos'),
    url(r'^proveedores/$', views.mostrar_proveedores, name='proveedores'),
    url(r'^facturacion/$', views.mostrar_facturacion, name='facturacion'),
    url(r'^proformas/$', views.mostrar_proformas, name='proformas'),
    url(r'^contactos/$', views.mostrar_contactos, name='contactos'),
    url(r'^elements/$', views.mostrar_elements),
    url(r'^index-video/$', views.mostrar_indexvideo),
    url(r'^services-single/$', views.mostrar_servicessingle),
    url(r'^clientes/$', views.mostrar_clientes, name= 'clientes'),
    url(r'^team/$', views.mostrar_team),
    url(r'^testimonials/$', views.mostrar_testimonials),
    url(r'^elements/$', views.mostrar_elements),
    url(r'^login/$',views.ingresar, name='login') 
    #url(r'^registro/$', core_views.singup, name='registro'),
]
