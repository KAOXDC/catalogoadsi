from django import forms
from catalogo.apps.ventas.models import Producto

class add_product_form(forms.ModelForm):
	class Meta:
		model   = Producto
		#se excluye el status por que en el modelo lo ponemos default=True
		exclude = {'status',} 



'''class add_product_form(forms.Form):
	nombre 		= forms.CharField(widget = forms.TextInput())
	descripcion = forms.CharField(widget = forms.Textarea())
	imagen		= forms.ImageField(required = False)
	precio		= forms.DecimalField(required = True)
	stock		= forms.IntegerField(required = True)
	
	def clean (self):
		return self.cleaned_data'''