from django.conf.urls import url

from .views import (ComissaoListView, ComissaoAtencaoListView, ComissaoCreateView,
					ComissaoUpdateView, ComissaoDeleteView)

urlpatterns = [
	url(r'atencao/$', ComissaoAtencaoListView.as_view(), name='comissao_atencao_list'),
 	url(r'list/$', ComissaoListView.as_view(), name='comissao_list'),
	url(r'cad/$', ComissaoCreateView.as_view(), name='comissao_create'),
	url(r'(?P<pk>\d+)/$', ComissaoUpdateView.as_view(), name='comissao_update'),
	url(r'(?P<pk>\d+)/delete/$', ComissaoDeleteView.as_view(), name='comissao_delete'),
]
