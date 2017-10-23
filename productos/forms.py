from django.forms import ModelForm
from .models import Producto
from django.contrib.admin import widgets
from django import forms

# Create the form class.
class ProductoForm(ModelForm):

	class Meta:
		model = Producto
		fields = ('__all__')
		widgets = {'fecha_vencimiento': forms.DateInput(attrs={'class': 'datepicker'})}