# Projeto de pesquisa de alunos do curso de Ciência da Computação com a Comissão de Projetos Científicos da Universidade Franciscana. O projeto está inserido no Laboratório de Práticas dos cursos de Informática da instituição.

## Preparando o ambiente para desenvolvimento
> ***Ocorrência:*** A cada nova instalação do Sistema Operacional.

### Instalação do PIP (Python Index Package):
```shell
#Linux/Mac OSx:
sudo easy_install pip

#Distribuições Linux derivados do Debian - Ex.: Ubuntu:
sudo apt-get install python-pip
```

### Instalação do Virtualenv (Ferramenta gestora de ambientes Python virtualizados isolados):
```shell
#Linux/Mac OSx:
pip install virtualenv

#Distribuições Linux derivados do Debian - Ex.: Ubuntu:
sudo apt-get install python-virtualenv
```
### Instalação do GIT (Habilitar o Sistema Operacional para trabalhar com controle de versão GIT)
```shell
#Mac OS/x:
http://sourceforge.net/projects/git-osx-installer/

#Distribuições Linux derivados do Debian - Ex.: Ubuntu:
sudo apt-get install git
```

## Criação do projeto:
> Passo a passo com principais atividades necessárias para iniciar um projeto. Consulte a documentação oficial do Django para mais detalhes https://www.djangoproject.com/start/

> ***Objetivo:*** Projeto Django rodando localmente, versionado com Git e distribuído na plataforma Github

```shell
#Criando o diretorio que conterá os recursos necessários para execução, desenvolvimento e distribuição do projeto
mkdir comic

#Acessando o diretório principal
cd comic

#Criando uma virtualenv com Python (ambiente isolado) - Ambiente localizado no diretório venv
virtualenv -p python3 venv

#Ativando a virtualenv
source venv/bin/activate

#Ativando a virtualenv no Windows
venv\Scripts\activate

#Instalando os softwares dentro do arquivo requirements.txt
pip install -r requirements.txt

Django==2.1.2
django-bootstrap3==9.1.0
mysqlclient==1.3.13
python-decouple==3.1
dj-database-url==0.5.0


#Iniciando um projeto Django
django-admin.py startproject projeto

#Acessando o diretório projeto
cd projeto

#Configurando a linguagem e data/hora do projeto. Edite o arquivo: projeto/settings.py
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'


#TEM INFORMAÇÕES A MAIS==========================



#Rodar a migração para criação das tabelas básicas do Django no Banco de dados
python manage.py migrate

#Criando o super usuário para acessar o Django Admin (Painel administrativo do site) via autenticação
python manage.py createsuperuser

#Criação de uma aplicação chamada core
python manage.py startapp core

#Criacao da view responsável pela exibição da home/index na app core
#edite o arquivo core/views.py e certifique-se que contenha:

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.base import TemplateView

from utils.decorators import LoginRequiredMixin

class HomeView(LoginRequiredMixin, TemplateView):
	template_name = 'core/home.html'

class AboutView(TemplateView):
	template_name = 'core/about.html'


#crie o home.html em core/templates/core/home.html (será preciso criar os diretórios)

{% extends 'core/base.html' %}
{% load bootstrap3 %}
{% load static %}

{% block title %}
	{% bootstrap_icon 'user' %} Home
{% endblock %}

{% block content %}

{% if user.is_authenticated %}
	<center>
		<a href= "http://www.universidadefranciscana.edu.br" target="_blank">
			<img src="{% static 'core/img/logoUFN_hor.jpg' %}"
     	 		 class="img-responsive" style="max-width: 340px;">
     	</a>

     	 <h2>Sistema de Gestão de Projetos junto à COMIC - UFN</h2>
     	 
     	 <h4>Professor Responsável: Huander Andreolla </h4>
	</center>

{% endif %}

<!-- {% bootstrap_icon "time" %}
-->
{% endblock %}



#crie o arquivo urls.py em: core/urls.py Ele é responsável pela identificação da view responsável para cada URL pertencente a app core

#edite o arquivo core/urls.py com o seguinte conteúdo:

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from .views import HomeView, AboutView

urlpatterns = [
   url(r'^$', HomeView.as_view(), name='home'),
   url(r'^about$', AboutView.as_view(), name='about'),
]


#instale a app core no projeto editando o arquivo projeto/settings.py adicionando na lista INSTALLED_APPS como no exemplo:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'core',
]

#habilite o gerenciador de URLs do projeto para trabalhar com as URLs da app core, para isto, edite o arquivo projeto/urls.py importando o urls do core:

# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

#url para arquivos de media quando em desenvolvimento
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, 
    document_root = settings.STATIC_ROOT)    


#neste ponto a sua home já pode ser exibida no navegador

#rodando o servidor web de desenvolvimento (dentro do diretório projeto)
python manage.py runserver

#acessando via navegador
http://localhost:8000
```


## Criando modelo para persistir no Banco de Dados, Instalando a app no Django Admin (Painel), Buscando os registros do modelo numa view e mostrando no HTML
```shell
#no diretório projeto, dentro de enfermagem, crie as apps: usuario, instituicao, injuria, pergunta, midia, resposta e acao

python manage.py startapp usuario
python manage.py startapp instituicao
python manage.py startapp ....

#edite o arquivo models.py dentro da app criada, adicionando a classe referente a app. Repita isso para cada models de aplicação criada

#edite o arquivo views.py dentro da app criada, adicionando os métodos referentes a app. Repita isso para cada classe de aplicação criada. Por exemplo:

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ClasseCriada

class ClasseCriadaListView(LoginRequiredMixin, ListView):
	model = ClasseCriada

class ClasseCriadaCreateView(LoginRequiredMixin, CreateView):
	model = ClasseCriada
	fields = ['campo1', 'campo2', 'campo3' ,'....']
	success_url = 'app_criada_list'

class ClasseCriadaUpdateView(LoginRequiredMixin, UpdateView):
	model = ClasseCriada
	fields = ['campo1', 'campo2', 'campo3' ,'....']
	success_url = 'app_criada_list'

class InjuriaDeleteView(LoginRequiredMixin, DeleteView):
	model = ClasseCriada
	fields = ['campo1', 'campo2', 'campo3' ,'....']


#instale a app criada no projeto editando o arquivo projeto/settings.py adicionando na lista INSTALLED_APPS:

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'core',
	'usuario',
	'instituicao',
	'...'
]

#habilite o gerenciador de URLs do projeto para trabalhar com as URLs da app criada. Para isto, edite o arquivo projeto/urls.py importando o urls da app criada:

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls')),
    url(r'usuario/', include('usuario.urls')),
    url(r'instituicao/', include('instituicao.urls')),
    url(r'.../', include('....urls')),
    url(r'^accounts/', include('django.contrib.auth.urls'))
]

#crie o arquivo urls.py dentro da pasta da app criada. Por exemplo:

from django.conf.urls import url
from .views import ClasseCriadaListView, ClasseCriadaCreateView
from .views import ClasseCriadaUpdateView, ClasseCriadaDeleteView


urlpatterns = [
	url(r'list/$', ClasseCriadaListView.as_view(), name='app_criada_list'),
	url(r'cad/$', ClasseCriadaCreateView.as_view(), name='app_criada_create'),
	url(r'(?P<pk>\d+)/$', ClasseCriadaUpdateView.as_view(), name='app_criada_update'),
	url(r'(?P<pk>\d+)/delete/$', ClasseCriadaDeleteView.as_view(), name='app_criada_delete'),
]

#criar script para migração do Banco de Dados dos modelos das apps (script que cria as tabelas necessárias para atender o modelo especificado)

python manage.py makemigrations core
python manage.py makemigrations usuario
python manage.py makemigrations ...

#comando no shell para rodar as migrações da app core no Banco de Dados
python manage.py migrate core
python manage.py migrate usuario
python manage.py migrate ....

```
## Dicas - Trabalhando com Querysets
> ***Mais detalhes na documentação oficial do Django:*** https://docs.djangoproject.com/en/1.11/ref/models/querysets/
