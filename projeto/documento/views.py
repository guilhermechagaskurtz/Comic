from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse

from utils.decorators import LoginRequiredMixin

from .models import Documento


class DocumentoListView(LoginRequiredMixin, ListView):
    model = Documento


class DocumentoCreateView(LoginRequiredMixin, CreateView):
    model = Documento
    fields = ['descricao_arquivo', 'arquivo', 'is_active']
    success_url = 'documento_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Documento cadastrado com sucesso na plataforma!')
        return reverse(self.success_url)


class DocumentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Documento
    fields = ['descricao_arquivo', 'arquivo', 'is_active']
    success_url = 'documento_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Documento atualizado com sucesso na plataforma!')
        return reverse(self.success_url) 


class DocumentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Documento
    success_url = 'documento_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à esse curso, permissão negada!')
        return redirect(self.success_url)