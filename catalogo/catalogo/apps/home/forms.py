from django import forms

class contact_form(forms.Form):
	correo 	= forms.EmailField(widget = forms.TextInput())
	titulo 	= forms.CharField(widget = forms.TextInput())
	texto 	= forms.CharField(widget = forms.Textarea())

class Login_form(forms.Form):
	usuario  = forms.CharField(widget = forms.TextInput())
	clave = forms.CharField(widget = forms.PasswordInput(render_value = False))