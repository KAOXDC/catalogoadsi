# Vistas de la aplicaion ventas
from django.shortcuts import render_to_response
from django.template import RequestContext
from catalogo.apps.ventas.forms import add_product_form
from catalogo.apps.ventas.models import Producto
from django.http import HttpResponseRedirect

def add_product_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_product_form(request.POST, request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.status = True
			add.save() # guarda la informacion
			formulario.save_m2m() # guarda las relaciones ManyToMany
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/producto/%s' %add.id)
	else:
		formulario = add_product_form()
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('ventas/add_producto.html', ctx,context_instance = RequestContext(request))

def edit_product_view(request, id_prod):
	info = ""
	prod = Producto.objects.get(pk = id_prod)
	if request.method == "POST":
		formulario = add_product_form(request.POST, request.FILES, instance= prod)
		if formulario.is_valid():
			edit_prod = formulario.save(commit = False)
			formulario.save_m2m()
			edit_prod.status = True
			edit_prod.save()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect('/producto/%s'% edit_prod.id)
	else:
		formulario = add_product_form(instance = prod)
	ctx = {'form':formulario, 'informacion':info}
	return render_to_response('ventas/edit_producto.html', ctx,context_instance = RequestContext(request))




def del_product_view(request, id_prod):
	info = "inicializando"
	try:
		prod = Producto.objects.get(pk = id_prod)
		prod.delete()
		info = "Producto Eliminado Correctamente"
		return HttpResponseRedirect('/productos/')	
	except:
		info = "Producto no se puede Eliminar"
		#return render_to_response('home/productos.html', context_instance = RequestContext(request))
		return HttpResponseRedirect('/productos/')	
	



'''
def add_product_view(request):
	if request.method == "POST": # si es POST
		formulario = add_product_form(request.POST, request.FILES)
		informacion = "inicializando"
		if formulario.is_valid():
			nombre 		= formulario.cleaned_data['nombre']
			descripcion = formulario.cleaned_data['descripcion']
			imagen 		= formulario.cleaned_data['imagen']
			precio 		= formulario.cleaned_data['precio']
			stock 		= formulario.cleaned_data['stock']
			p = Producto()
			p.nombre = nombre
			p.descripcion = descripcion
			p.status = True
			if imagen:
				p.imagen = imagen
			p.precio = precio
			p.stock = stock
			p.save() # Guarda la informacion 
			informacion = "se guardo satisfactoriamente"
		else:
			info = "informacion con datos incorrectos"
		formulario = add_product_form()
		ctx = {'form':formulario, 'info': informacion}
		return render_to_response('ventas/add_producto.html', ctx,context_instance = RequestContext(request))
	else: # si es GET
		formulario =  add_product_form()
		ctx = {'form':formulario}
		return render_to_response('ventas/add_producto.html', ctx,context_instance = RequestContext(request))
'''
'''
def edit_product_view(request, id_prod):
	p = Producto.objects.get(id = id_prod)

	if request.method == "POST":
		formulario = add_product_form(request.POST, request.FILES)
		if formulario.is_valid():
			nombre 		= formulario.cleaned_data['nombre']
			descripcion = formulario.cleaned_data['descripcion']
			imagen 		= formulario.cleaned_data['imagen']
			precio 		= formulario.cleaned_data['precio']
			stock 		= formulario.cleaned_data['stock']
			p.nombre = nombre
			p.descripcion = descripcion
			p.status = True
			if imagen:
				p.imagen = imagen
			p.precio = precio
			p.stock = stock
			p.save() # Guarda la informacion 
			informacion = "se guardo satisfactoriamente"
			return HttpResponseRedirect ('/producto/%s'%p.id)

	if request.method == "GET":
		formulario = add_product_form(initial = {
										'nombre' : p.nombre,
										'descripcion' : p.descripcion,
										'precio' : p.precio,
										'stock' : p.stock,	})
	ctx = {'form':formulario, 'producto':p}
	return render_to_response('ventas/edit_producto.html',ctx ,context_instance = RequestContext(request))
'''


'''0786
380400'''