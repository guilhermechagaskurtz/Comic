from datetime import datetime
# from __future__ import unicode_literals
from django.shortcuts import render
from django.urls import reverse
from django.http import Http404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from utils.decorators import LoginRequiredMixin

from .models import Submissao
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect

from edital.models import Edital

from .models import Submissao
from .forms import SubmissaoForm, BuscaSubmissaoForm

class SubmissaoListView(LoginRequiredMixin, ListView):
    model = Submissao 
    template_name = 'submissao/submissao_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaSubmissaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaSubmissaoForm()
        return context

    def get_queryset(self):
        qs = Submissao.objects.all()

        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaSubmissaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaSubmissaoForm()

        if form.is_valid():
            edital = form.cleaned_data.get('edital')
            titulo = form.cleaned_data.get('titulo')
            status = form.cleaned_data.get('status')
            nome_integrante = form.cleaned_data.get('nome_integrante')
            
            if edital:
                qs = qs.filter(edital=edital)
            
            if titulo:
                qs = qs.filter(titulo__icontains=titulo)    
            
            if status:
                qs = qs.filter(avaliacao__comissao__status=status)
                
            if nome_integrante:
                qs = qs.filter(Q(responsavel__nome__icontains=nome_integrante) | Q(colaborador__nome__icontains=nome_integrante))

        return qs


    
class SubmissaoAtencaoListView(LoginRequiredMixin, ListView):
    model = Submissao
    template_name = 'submissao/submissao_atencao_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaSubmissaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaSubmissaoForm()
        return context

    def get_queryset(self):
        qs = Submissao.objects.all()

        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaSubmissaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaSubmissaoForm()

        if form.is_valid():
            edital = form.cleaned_data.get('edital')
            titulo = form.cleaned_data.get('titulo')
            status = form.cleaned_data.get('status')
            nome_integrante = form.cleaned_data.get('nome_integrante')
            
            if edital:
                qs = qs.filter(edital=edital)
            
            if titulo:
                qs = qs.filter(titulo__icontains=titulo)    
            
            if status:
                qs = qs.filter(avaliacao__comissao__status=status)
                
            if nome_integrante:
                qs = qs.filter(Q(responsavel__nome__icontains=nome_integrante) | Q(colaborador__nome__icontains=nome_integrante))

        return qs

    
class SubmissaoAprovadoListView(LoginRequiredMixin, ListView):
    model = Submissao
    template_name = 'submissao/submissao_aprovado_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaSubmissaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaSubmissaoForm()
        return context

    def get_queryset(self):
        qs = Submissao.objects.all()

        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaSubmissaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaSubmissaoForm()

        if form.is_valid():
            edital = form.cleaned_data.get('edital')
            titulo = form.cleaned_data.get('titulo')
            status = form.cleaned_data.get('status')
            nome_integrante = form.cleaned_data.get('nome_integrante')
            
            if edital:
                qs = qs.filter(edital=edital)
            
            if titulo:
                qs = qs.filter(titulo__icontains=titulo)    
            
            if status:
                qs = qs.filter(avaliacao__comissao__status=status)
                
            if nome_integrante:
                qs = qs.filter(Q(responsavel__nome__icontains=nome_integrante) | Q(colaborador__nome__icontains=nome_integrante))

        return qs


class SubmissaoCreateView(LoginRequiredMixin, CreateView):
    model = Submissao
    form_class = SubmissaoForm
    success_url = 'submissao_list'


class SubmissaoUpdateView(LoginRequiredMixin, UpdateView):
    model = Submissao
    form_class = SubmissaoForm
    success_url = 'submissao_list'
    
    def form_valid(self, form):
        try:
            submissao = form.save(commit=False)
            submissao.dt_atualizacao_submissao = datetime.now()
            submissao.save()
            self.object = submissao
        except Exception as e:
            messages.error(self.request, 'Erro ao atualizar o projeto. %s' % e)
        
        return super(SubmissaoUpdateView, self).form_valid(form)


class SubmissaoPendenteUpdateView(LoginRequiredMixin, UpdateView):
    model = Submissao
    fields = ['arquivo_atualizacao_pendencia_projeto']
    template_name = 'submissao/submissao_corrigir_form.html'
    success_url = 'submissao_list'

    def get_object(self,queryset=None):
        obj = super().get_object(queryset)
        return obj
    
    def get_success_url(self):
        return reverse(self.success_url)
    

class SubmissaoAprovadoUpdateView(LoginRequiredMixin, UpdateView):
    model = Submissao
    fields = ['arquivo_comite_etica', 'arquivo_relatorio_parcial', 'arquivo_relatorio_final', 
              'registros_apos_aprovacao', 'arquivo_emenda1', 'arquivo_emenda2', 'arquivo_emenda3']
    template_name = 'submissao/submissao_aprovado_form.html'
    success_url = 'submissao_aprovado_list'

    def get_object(self,queryset=None):
        obj = super().get_object(queryset)
        return obj
    
    def get_success_url(self):
        return reverse(self.success_url)

class SubmissaoDeleteView(LoginRequiredMixin, DeleteView):
    model = Submissao
    success_url = 'submissao_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(request, 'Submissão excluída com sucesso!')
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à essa submissão, permissão negada!')
        return redirect(self.success_url)

class SubmissaoEditalListView(LoginRequiredMixin, ListView):
    model = Submissao
    template_name = 'submissao/submissao_edital_list.html'

    def get_queryset(self):
        edital = Edital.objects.get(id=self.kwargs.get('pk_edital'))
        situacao = self.kwargs.get('situacao')
        print(situacao)
        if situacao == 'APROVADAS':
            return edital.submissoes_aprovadas
        elif situacao == 'REPROVADAS':
            return edital.submissoes_reprovadas
        elif situacao == 'TODAS':
            return edital.submissoes

    def get_context_data(self):
        context = super().get_context_data()
        context['edital'] = Edital.objects.get(pk=self.kwargs['pk_edital'])
        context['situacao'] = self.kwargs.get('situacao')
        return context