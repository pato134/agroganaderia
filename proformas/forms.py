from django.forms import ModelForm
from .models import Proforma
from django import forms

class ProformaForm(forms.ModelForm):
	class Meta:
		model = Proforma
		fields = ['fecha', 'iva', 'total']