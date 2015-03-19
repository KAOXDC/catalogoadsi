from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import settings
'''
from rest_framework import routers
from catalogo.apps.webservices.ws_productos.view import producto_viewset
router = routers.DefaultRouter()
router.register(r'links', producto_viewset)

'''
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'catalogo.views.home', name='home'),
    # url(r'^catalogo/', include('catalogo.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('catalogo.apps.home.urls')), #incluye las ulrs de la app home
    url(r'^',include('catalogo.apps.ventas.urls')),
    url(r'^',include('catalogo.apps.webservices.ws_productos.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
#        url(r'^api/', include(router.urls)),

#url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)



