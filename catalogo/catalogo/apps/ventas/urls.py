from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('catalogo.apps.ventas.views',
		url(r'^add/producto/$','add_product_view',name = 'vista_agregar_producto'),
		url(r'^edit/producto/(?P<id_prod>.*)/$', 'edit_product_view', name = 'vista_editar_producto'),
		url(r'^del/producto/(?P<id_prod>.*)/$', 'del_product_view', name = 'vista_eliminar_producto'),
		url(r'^del/marca/(?P<id_marca>.*)/$', 'del_marca_view', name = 'vista_eliminar_marca'),
		
	)

		