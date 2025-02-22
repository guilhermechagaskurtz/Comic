"""projeto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core.urls')),
    url(r'instituicao/', include('instituicao.urls')),
    url(r'usuario/', include('usuario.urls')),
    url(r'edital/', include('edital.urls')),
    url(r'submissao/', include('submissao.urls')),
    url(r'avaliacao/', include('avaliacao.urls')),
    url(r'appprofessor/', include('appprofessor.urls')),
    url(r'comissao/', include('comissao.urls')),
    url(r'documento/', include('documento.urls')),
    url(r'aviso/', include('aviso.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]

#media url
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)