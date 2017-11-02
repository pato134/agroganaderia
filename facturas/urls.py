from django.conf.urls import url, include
from . import views

urlpatterns = [
	#url(r'^$', views.mostrar_inicio),
	
    url(r'^nueva/$', views.factura_nuevo, name='factura_crear'),
    url(r'^list/$', views.factura_list, name='factura_list'),
    url(r'^ver/(?P<id_factura>\d+)$', views.ver_factura, name='ver'),

]