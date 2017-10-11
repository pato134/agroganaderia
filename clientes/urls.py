from django.conf.urls import url, include
from . import views

urlpatterns = [
	#url(r'^$', views.mostrar_inicio),
	
    url(r'^clientes/$', views.mostrar_clientes, name= 'clientes'),
    url(r'^registrarse/$', views.registrarse, name= 'registrarse'),
    
]