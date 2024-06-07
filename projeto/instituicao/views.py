# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from utils.decorators import LoginRequiredMixin
from .models import Instituicao
from django.contrib import messages

# Create your views here.

class InstituicaoListView(LoginRequiredMixin, ListView):
    model = Instituicao


class InstituicaoCreateView(LoginRequiredMixin, CreateView):
    model = Instituicao
    fields = ['nome', 'sigla','site','contato','email','telefone']
    success_url = 'instituicao_list'


class InstituicaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Instituicao
    fields = ['nome', 'sigla','site','contato','email','telefone']
    success_url = 'instituicao_list'


class InstituicaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Instituicao
    success_url = 'instituicao_list'

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
            messages.error(request, 'Há dependências ligadas à essa instituição, permissão negada!')
        return redirect(self.success_url)