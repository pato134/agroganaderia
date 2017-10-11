from django.conf.urls import url, include
from . import views

urlpatterns = [
	
  url(r'^listar_quienessomos/$', views.listar_quienessomos, name='listar_quienessomos'),
]