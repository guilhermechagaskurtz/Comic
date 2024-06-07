from __future__ import unicode_literals

from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from utils.decorators import LoginRequiredMixin

from datetime import datetime

from .models import Comissao
from .forms import BuscaComissaoForm
from avaliacao.models import Avaliacao


class ComissaoListView(LoginRequiredMixin, ListView):
    model = Comissao
    template_name = 'comissao/comissao_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaComissaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaComissaoForm()
        return context

    def get_queryset(self):
        qs = Comissao.objects.all()

        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaComissaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaComissaoForm()

        if form.is_valid():
            edital = form.cleaned_data.get('edital')
            titulo = form.cleaned_data.get('titulo')
            status = form.cleaned_data.get('status')
            nome_integrante = form.cleaned_data.get('nome_integrante')
            
            if edital:
                    qs = qs.filter(avaliacao_comissao__submissao__edital=edital)
            
            if titulo:
                qs = qs.filter(avaliacao_comissao__submissao__titulo__icontains=titulo)    
            
            if status:
                qs = qs.filter(status=status)
                
            if nome_integrante:
                qs = qs.filter(Q(avaliacao_comissao__submissao__responsavel__nome__icontains=nome_integrante) | Q(avaliacao_comissao__submissao__colaborador__nome__icontains=nome_integrante))

        return qs

class ComissaoAtencaoListView(LoginRequiredMixin, ListView):
    model = Comissao
    template_name = 'comissao/comissao_atencao_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaComissaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaComissaoForm()
        return context

    def get_queryset(self):
        qs = Comissao.objects.all()

        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaComissaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaComissaoForm()

        if form.is_valid():
            edital = form.cleaned_data.get('edital')
            titulo = form.cleaned_data.get('titulo')
            status = form.cleaned_data.get('status')
            nome_integrante = form.cleaned_data.get('nome_integrante')
            
            if edital:
                qs = qs.filter(avaliacao_comissao__submissao__edital=edital)
            
            if titulo:
                qs = qs.filter(avaliacao_comissao__submissao__titulo__icontains=titulo)    
            
            if status:
                qs = qs.filter(status=status)
                
            if nome_integrante:
                qs = qs.filter(Q(avaliacao_comissao__submissao__responsavel__nome__icontains=nome_integrante) | Q(avaliacao_comissao__submissao__colaborador__nome__icontains=nome_integrante))

        return qs

class ComissaoCreateView(LoginRequiredMixin, CreateView):
    model = Comissao
    template_name = 'comissao/comissao_form_create.html'
    fields = ['avaliacao_comissao']
    success_url = 'comissao_list'

    def get_initial(self):
        initials = super().get_initial()
        initials['avaliacao_comissao'] = Avaliacao.objects.get(id=self.request.GET.get('avaliacao_id'))
        return initials

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avaliacao_comissao'] = Avaliacao.objects.get(id=self.request.GET.get('avaliacao_id'))
        return context

    def form_valid(self, form):
        comissao = form.save()
        comissao.dt_avaliacao_comissao = datetime.now()
        comissao.save()
        return super(ComissaoCreateView, self).form_valid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'Instância de parecer criada com sucesso!! Assim que puder, finalize-o!')
        return reverse(self.success_url)

class ComissaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Comissao
    fields = ['status', 'arquivo_parecer_comissao','arquivo_parecer_comissao_pendencia', 'comentario']
    success_url = 'comissao_list'

    def form_valid(self, form):
        comissao = form.save()
        comissao.dt_avaliacao_comissao = datetime.now()
        comissao.save()
        return super(ComissaoUpdateView, self).form_valid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'Parecer atualizado com sucesso!!')
        return reverse(self.success_url)

class ComissaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Comissao
    success_url = 'comissao_list'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()		
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(request, 'Parecer excluído com sucesso!')
        except Exception as e:
            messages.error(request, 'Há dependências ligadas ao parecer, permissão negada!')
        return redirect(self.success_url)
