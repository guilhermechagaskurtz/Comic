from django.conf.urls import url

from .views import AvisoListView, AvisoCreateView
from .views import AvisoUpdateView, AvisoDeleteView, AvisoEnviaEmail


urlpatterns = [
	url(r'list/$', AvisoListView.as_view(), name='aviso_list'),
	url(r'cad/$', AvisoCreateView.as_view(), name='aviso_create'),
	url(r'(?P<pk>\d+)/$', AvisoUpdateView.as_view(), name='aviso_update'),
	url(r'(?P<pk>\d+)/delete/$', AvisoDeleteView.as_view(), name='aviso_delete'),
	url(r'(?P<pk>\d+)/envia-email/$', AvisoEnviaEmail.as_view(), name='aviso_envia_email'),
]
