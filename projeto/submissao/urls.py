from django.conf.urls import url

from .views import (SubmissaoListView, SubmissaoAprovadoListView , SubmissaoAtencaoListView, SubmissaoCreateView,
					SubmissaoUpdateView, SubmissaoAprovadoUpdateView, SubmissaoPendenteUpdateView, SubmissaoDeleteView, 
					SubmissaoEditalListView)

urlpatterns = [
	url(r'edital/list/(?P<pk_edital>\d+)/(?P<situacao>[\w|\W]+)', SubmissaoEditalListView.as_view(), name='submissao_edital_list'),
 	url(r'aprovado/$', SubmissaoAprovadoListView.as_view(), name='submissao_aprovado_list'),
	url(r'atencao/$', SubmissaoAtencaoListView.as_view(), name='submissao_atencao_list'),
	url(r'list/$', SubmissaoListView.as_view(), name='submissao_list'),
	url(r'cad/$', SubmissaoCreateView.as_view(), name='submissao_create'),
	url(r'pendente/(?P<pk>\d+)/$', SubmissaoPendenteUpdateView.as_view(), name='submissao_pendente_update'),
 	url(r'aprovado/(?P<pk>\d+)/$', SubmissaoAprovadoUpdateView.as_view(), name='submissao_aprovado_update'),
	url(r'(?P<pk>\d+)/$', SubmissaoUpdateView.as_view(), name='submissao_update'),
	url(r'(?P<pk>\d+)/delete/$', SubmissaoDeleteView.as_view(), name='submissao_delete'),
]
