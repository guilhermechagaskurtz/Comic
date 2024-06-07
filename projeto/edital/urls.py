from django.conf.urls import url
from .views import EditalListView, EditalCreateView
from .views import EditalUpdateView, EditalDeleteView

urlpatterns = [
    url(r'list/$', EditalListView.as_view(), name='edital_list'),
    url(r'cad/$', EditalCreateView.as_view(), name='edital_create'),
    url(r'(?P<pk>\d+)/$', EditalUpdateView.as_view(), name='edital_update'),
    url(r'(?P<pk>\d+)/delete/$', EditalDeleteView.as_view(), name='edital_delete'),
]
