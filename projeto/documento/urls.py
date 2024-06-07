from django.conf.urls import url

from .views import DocumentoListView, DocumentoCreateView
from .views import DocumentoUpdateView, DocumentoDeleteView


urlpatterns = [
	url(r'list/$', DocumentoListView.as_view(), name='documento_list'),
	url(r'cad/$', DocumentoCreateView.as_view(), name='documento_create'),
	url(r'(?P<pk>\d+)/$', DocumentoUpdateView.as_view(), name='documento_update'),
	url(r'(?P<pk>\d+)/delete/$', DocumentoDeleteView.as_view(), name='documento_delete'),
]
