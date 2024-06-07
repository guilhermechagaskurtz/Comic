from django.urls import reverse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from utils.decorators import LoginRequiredMixin, StaffRequiredMixin
from usuario.models import Usuario

from aviso.models import Aviso

class HomeRedirectView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, **kwargs):
        if self.request.user.tipo == 'ADMINISTRADOR':
            return reverse('home')
        elif self.request.user.tipo == 'PROFESSOR':
            return reverse('appprofessor_home')

class HomeView(LoginRequiredMixin, StaffRequiredMixin, TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avisos'] = Aviso.ativos.filter(destinatario__in=[self.request.user.tipo, 'TODOS'])[0:2]
        return context

class AboutView(LoginRequiredMixin, StaffRequiredMixin,TemplateView):
    template_name = 'core/about.html'
