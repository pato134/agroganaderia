from django.forms import ModelForm
from .models import Producto

# Create the form class.
class ProductoForm(ModelForm):

	class Meta:
		model = Producto
		fields = ('__all__')