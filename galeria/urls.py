from django.conf.urls import url, include
from . import views

urlpatterns = [
	#url(r'^$', views.mostrar_inicio),
	
    url(r'^nuevo/$', views.imagen_nuevo, name='imagen_crear'),
]  