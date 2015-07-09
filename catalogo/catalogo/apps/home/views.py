# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from catalogo.apps.ventas.models import Producto
from catalogo.apps.home.forms import contact_form, Login_form
from django.core.mail import EmailMultiAlternatives # enviamos HTML
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage #paginacion 

def index_view (request):
	return render_to_response('home/index.html', context_instance = RequestContext(request))

def about_view (request):
	mensaje = "este es un mensaje desde mi vista"
	ctx = {'msg': mensaje}
	return render_to_response('home/about.html', ctx, context_instance = RequestContext(request))

"""def productos_view(request, pagina):
	lista_prod = Producto.objects.filter(status = True) # SELECT * FROM Producto WHERE status = True
	paginator = Paginator(lista_prod, 3)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		productos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		productos = paginator.page(paginator.num_pages)

	ctx = {'productos':productos}
	return render_to_response ('home/productos2.html', ctx, context_instance = RequestContext(request))"""

def contacto_view (request):
	info_enviado = False #Definir  si se envio la informacion o no se envio
	email = ""
	title = ""
	text  = ""
	if request.method == "POST": # evalua si el metodo fue POST
		formulario = contact_form(request.POST) #instancia del formulario con los datos ingresados
		if formulario.is_valid(): #evalua si el formulario es valido 
			info_enviado = True #la informacion se envio correctamente
			email = formulario.cleaned_data['correo'] # copia el correo ingresado en email 
			title = formulario.cleaned_data['titulo'] # copia el titulo ingresado en title
			text  = formulario.cleaned_data['texto']  # copia el texto ingresado en text
			''' Bloque conficugracion de envio por GMAIL  '''
			to_admin = 'kaoxdc@gmail.com'
			html_content = "Informacio recibida de %s <br> ---Mensaje--- <br> %s"%(email,text)
			msg = EmailMultiAlternatives('correo de contacto', html_content, 'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html') #definimos el contenido como HTML
			msg.send() #enviamos el correo
			''' Fin del Bloque '''
	else: #si no fue POST entonces fue  el metodo GET mostrara un formulario vacio
		formulario = contact_form() # creacion del formulario vacio
	ctx = {'form':formulario, 'email':email, "title":title, "text":text, "info_enviado":info_enviado}
	return render_to_response('home/contacto.html',ctx,context_instance = RequestContext(request))

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated(): #verificamos si el usuario ya esta authenticado o logueado  
		return HttpResponseRedirect('/') #si esta logueado lo redirigimos a la pagina principal 
	else: #si no esta authenticado
		if request.method == "POST": 
			formulario = Login_form(request.POST) #creamos un objeto de Loguin_form
			if formulario.is_valid(): # si la informacion enviada es correcta
				usu = formulario.cleaned_data['usuario'] #guarda informacion ingresada del formulario
				pas = formulario.cleaned_data['clave'] #guarda informacion ingresada del formulario
				usuario = authenticate(username = usu, password = pas)#asigna la autenticacion del usuario
				if usuario is not None and usuario.is_active:# si el usuario no es nulo y esta activo
					login(request, usuario) #se loguea al sistema con la informacion de usuario
					return HttpResponseRedirect('/productos/')# redirigimos a la pagina principal
				else:
					mensaje = "usuario y/o clave incorrecta"
		formulario = Login_form() #creamos un formulario nuevo en limpio
		ctx = {'form':formulario, 'mensaje':mensaje} # variable de contexto para pasar info a login.html
		return render_to_response('home/login.html', ctx, context_instance = RequestContext(request))

def logout_view(request):
	logout(request) #funcionde django importada anteriormente
	return HttpResponseRedirect('/') # redirigimos a la pagina principal


def single_product_view(request, id_prod):
	prod = Producto.objects.get(id = id_prod)
	cat  = prod.categorias.all() #obtenemos las categorias del producto encontrado
	ctx = {'producto':prod, 'categorias':cat}
	return render_to_response('home/single_producto.html',ctx,context_instance = RequestContext(request))

def register_view(request):
	form = Register_form()
	ctx = {'form':form}
	return render_to_response('home/register.html',ctx,context_instance=RequestContext(request))



def productos_view(request):
	lista_prod = Producto.objects.filter(status = True) # SELECT * FROM Producto WHERE status = True
	ctx = {'productos':lista_prod}
	return render_to_response ('home/productos2.html', ctx, context_instance = RequestContext(request))

