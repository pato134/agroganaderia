from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [


   url(r'^proveedor_crear/$', views.proveedor_nuevo, name='proveedor_crear'),
   url(r'^listar_proveedor/$', views.proveedor_nuevo, name='listar_proveedor'),

	
]