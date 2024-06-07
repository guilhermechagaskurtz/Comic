from __future__ import unicode_literals

from django.contrib import messages
from django.db.models import Q
from django.http import Http404, JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from utils.decorators import LoginRequiredMixin

from .models import Avaliacao
from .forms import AvaliacaoForm, BuscaAvaliacaoForm
from submissao.models import Submissao


class AvaliacaoListView(LoginRequiredMixin, ListView):
    model = Avaliacao
    template_name = 'avaliacao/avaliacao_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaAvaliacaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaAvaliacaoForm()
        return context

    def get_queryset(self):
        qs = Avaliacao.objects.all()

        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaAvaliacaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaAvaliacaoForm()

        if form.is_valid():
            edital = form.cleaned_data.get('edital')
            titulo = form.cleaned_data.get('titulo')
            status = form.cleaned_data.get('status')
            nome_integrante = form.cleaned_data.get('nome_integrante')
            
            if edital:
                qs = qs.filter(submissao__edital=edital)
            
            if titulo:
                qs = qs.filter(submissao__titulo__icontains=titulo)    
            
            if status:
                qs = qs.filter(comissao__status=status)
                
            if nome_integrante:
                qs = qs.filter(Q(submissao__responsavel__nome__icontains=nome_integrante) | Q(submissao__colaborador__nome__icontains=nome_integrante))

        return qs
 
class AvaliacaoAtencaoListView(LoginRequiredMixin, ListView):
    model = Avaliacao
    template_name = 'avaliacao/avaliacao_atencao_list.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaAvaliacaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaAvaliacaoForm()
        return context

    def get_queryset(self):
        qs = Avaliacao.objects.all()

        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaAvaliacaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaAvaliacaoForm()

        if form.is_valid():
            edital = form.cleaned_data.get('edital')
            titulo = form.cleaned_data.get('titulo')
            status = form.cleaned_data.get('status')
            nome_integrante = form.cleaned_data.get('nome_integrante')
            
            if edital:
                qs = qs.filter(submissao__edital=edital)
            
            if titulo:
                qs = qs.filter(submissao__titulo__icontains=titulo)    
            
            if status:
                qs = qs.filter(comissao__status=status)
                
            if nome_integrante:
                qs = qs.filter(Q(submissao__responsavel__nome__icontains=nome_integrante) | Q(submissao__colaborador__nome__icontains=nome_integrante))

        return qs


class AvaliacaoCreateView(LoginRequiredMixin, CreateView):
    model = Avaliacao
    form_class = AvaliacaoForm
    success_url = 'avaliacao_list'
    
    def get_initial(self):
	    initials = super().get_initial()
	    initials['submissao'] = Submissao.objects.get(id=self.request.GET.get('submissao_id'))
	    return initials
    
    def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['submissao'] = Submissao.objects.get(id=self.request.GET.get('submissao_id'))
	    return context
 
    def get_success_url(self):
        messages.success(self.request, 'Avaliação do projeto criada com sucesso!')
        return reverse(self.success_url)


class AvaliacaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Avaliacao
    form_class = AvaliacaoForm
    success_url = 'avaliacao_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Dados da avaliação do projeto atualizados com sucesso!')
        return reverse(self.success_url)


class AvaliacaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Avaliacao
    success_url = 'avaliacao_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(request, 'Avaliação excluída com sucesso!')
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à essa avaliação, permissão negada!')
        return redirect(self.success_url)