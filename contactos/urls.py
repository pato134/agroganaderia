from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^nuevo/$', views.contactos_nuevo, name='contactos_crear'),
]