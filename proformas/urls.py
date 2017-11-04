from django.conf.urls import url, include
from . import views

urlpatterns = [
	#url(r'^$', views.mostrar_inicio),
	
    url(r'^nueva/$', views.proforma_nuevo, name='proforma_crear'),
    url(r'^list/$', views.proforma_list, name='proforma_list'),
    url(r'^ver/(?P<id_proforma>\d+)$', views.ver_proforma, name='ver'),
]