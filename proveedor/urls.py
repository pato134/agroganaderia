from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [


	url(r'^registro/$', views.proveedor_nuevo, name='registro'),
	url(r'^listar/$', views.proveedor_listar, name='proveedor_listar'),
	url(r'^eliminar/(?P<id_proveedor>\d+)$', views.proveedor_listar, name='proveedor_eliminar'),
	url(r'^editar/(?P<id_proveedor>\d+)$', views.proveedor_editar, name='proveedor_editar'),
]