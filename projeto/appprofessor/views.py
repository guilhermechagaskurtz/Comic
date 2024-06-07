from datetime import datetime

from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import ListView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.db.models import Q

from utils.decorators import LoginRequiredMixin, ProfessorRequiredMixin
from documento.models import Documento
from usuario.models import Usuario
from submissao.models import Submissao
from avaliacao.models import Avaliacao

from .forms import MinhaAvaliacaoResponsavelForm, MinhaAvaliacaoSuplenteForm
from .forms import SubmissaoForm, BuscaAvaliacaoForm, BuscaSubmissaoForm

from aviso.models import Aviso

class HomeRedirectView(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, **kwargs):
        if self.request.user.tipo == 'ADMINISTRADOR':
            return reverse('home')
        elif self.request.user.tipo == 'PROFESSOR':
            return reverse('appprofessor_home')


class HomeView(LoginRequiredMixin, ProfessorRequiredMixin, TemplateView):
    template_name = 'appprofessor/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avisos'] = Aviso.ativos.filter(destinatario__in=[self.request.user.tipo, 'TODOS'])[0:2]
        return context

class AboutView(LoginRequiredMixin, TemplateView, ProfessorRequiredMixin):
    template_name = 'appprofessor/about.html'


class DadosProfessorUpdateView(LoginRequiredMixin, ProfessorRequiredMixin, UpdateView):
    model = Usuario
    template_name = 'appprofessor/dados_professor_form.html'
    fields = ['nome', 'email','area_conhecimento_cnpq','curso_graduacao_vinculado','curso_pos_graduacao','grupo_pesquisa','data_nasc', 'cpf','rg','matricula', 'lattes', 'instituicao']
    success_url = 'appprofessor_home'
     
    def get_success_url(self):
        messages.success(self.request, 'Seus dados foram alterados com sucesso!')
        return reverse(self.success_url)
    

class SubmissaoListView(LoginRequiredMixin, ProfessorRequiredMixin, ListView):
    model = Submissao
    template_name = 'appprofessor/submissao_list.html'

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
        qs = qs.filter(responsavel = self.request.user)


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
    

class SubmissaoCreateView(LoginRequiredMixin, ProfessorRequiredMixin, CreateView):
    model = Submissao
    template_name = 'appprofessor/submissao_form.html'
    form_class = SubmissaoForm
    success_url = 'appprofessor_submissao_list'

    def form_valid(self, form):
        try:
            # messages.warning(self.request, 'PASSEI')
            submissao = form.save(commit=False)
            submissao.responsavel = self.request.user
            submissao.save()
            self.object = submissao
        except Exception as e:
            messages.error(self.request, 'Erro ao submeter o projeto. %s' % e)
        
        return super(SubmissaoCreateView, self).form_valid(form)
    
    def get_success_url(self):
        messages.success(self.request, 'Sua submissão foi gravada e enviada com sucesso!')
        return reverse(self.success_url)


class SubmissaoUpdateView(LoginRequiredMixin, ProfessorRequiredMixin, UpdateView):
    model = Submissao
    form_class = SubmissaoForm
    template_name = 'appprofessor/submissao_form.html'
    success_url = 'appprofessor_submissao_list'
    
    def form_valid(self, form):
        try:
            submissao = form.save(commit=False)
            submissao.dt_atualizacao_submissao = datetime.now()
            submissao.save()
            self.object = submissao
        except Exception as e:
            messages.error(self.request, 'Erro ao atualizar o projeto. %s' % e)
        
        return super(SubmissaoUpdateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Sua submissão foi alterada, gravada e enviada com sucesso!')
        return reverse(self.success_url)
    
    
class SubmissaoPendenteUpdateView(LoginRequiredMixin, ProfessorRequiredMixin, UpdateView):
    model = Submissao
    template_name = 'appprofessor/submissao_corrigir_form.html'
    fields = ['arquivo_atualizacao_pendencia_projeto']
    success_url = 'appprofessor_submissao_list'

    def get_object(self,queryset=None):
        obj = super().get_object(queryset)
        return obj
        
        # if obj.permite_corrigir:
        #     return obj
        # else:
        #     raise Http404()
    
    def get_success_url(self):
        return reverse(self.success_url)
    
class SubmissaoAprovadoUpdateView(LoginRequiredMixin, UpdateView):
    model = Submissao
    fields = ['arquivo_comite_etica', 'arquivo_relatorio_parcial', 'arquivo_relatorio_final', 
              'registros_apos_aprovacao', 'arquivo_emenda1', 'arquivo_emenda2', 'arquivo_emenda3']
    template_name = 'appprofessor/submissao_aprovado_form.html'
    success_url = 'appprofessor_submissao_list'

    def get_object(self,queryset=None):
        obj = super().get_object(queryset)
        return obj
    
    def form_valid(self, form):
        try:
            submissao = form.save(commit=False)
            submissao.dt_atualizacao_submissao = datetime.now()
            submissao.save()
            self.object = submissao
        except Exception as e:
            messages.error(self.request, 'Erro ao atualizar o projeto. %s' % e)
        
        return super(SubmissaoAprovadoUpdateView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse(self.success_url)


class SubmissaoDeleteView(LoginRequiredMixin, ProfessorRequiredMixin, DeleteView):
    model = Submissao
    template_name = 'appprofessor/submissao_confirm_delete.html'
    success_url = 'appprofessor_submissao_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        # success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(request, 'Sucesso em excluir sua submissão!')
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à essa submissão, permissão negada!')
        return redirect(self.success_url)

    def get(self, request, *args, **kwargs):
        try:
            submissao = Submissao.objects.get(id=kwargs['pk'])
            if submissao.responsavel != request.user:
                raise Exception('Você não tem permissão para deletar esta submissão!')
        except Exception as e:
            messages.error(request, e)
            return redirect(self.success_url)
        return super(SubmissaoDeleteView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        return reverse(self.success_url)
    

class MinhaAvaliacaoListView(LoginRequiredMixin, ProfessorRequiredMixin, ListView):
    model = Avaliacao
    template_name = 'appprofessor/minha_avaliacao_list.html'

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
        qs = super(MinhaAvaliacaoListView, self).get_queryset()
        qs = qs.filter(Q(avaliador_responsavel = self.request.user) | Q(avaliador_suplente = self.request.user))     


        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaAvaliacaoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaAvaliacaoForm()

        if form.is_valid():
            edital = form.cleaned_data.get('edital')
            titulo = form.cleaned_data.get('titulo')
            nome_integrante = form.cleaned_data.get('nome_integrante')
            
            if edital:
                qs = qs.filter(submissao__edital=edital)
            
            if titulo:
                qs = qs.filter(submissao__titulo__icontains=titulo)    
            
            if nome_integrante:
                qs = qs.filter(Q(submissao__responsavel__nome__icontains=nome_integrante) | Q(submissao__colaborador__nome__icontains=nome_integrante))

        return qs

class MinhaAvaliacaoResponsavelUpdateView(LoginRequiredMixin, ProfessorRequiredMixin, UpdateView):
    model = Avaliacao
    form_class = MinhaAvaliacaoResponsavelForm
    template_name = 'appprofessor/minha_avaliacao_responsavel_form.html'
    success_url = 'appprofessor_minha_avaliacao_list'

    def get_object(self, queryset=None):
        """
        Não deixa entrar no formulário de avaliação se ele não foi designado como 
        avaliador responsável
        """
        pk = self.kwargs.get('pk')
        try:
            obj = Avaliacao.objects.get(pk=pk, avaliador_responsavel=self.request.user)
        except:
            raise Http404("Você não foi designado como avaliador responsável para esta submissão")
        return obj

    def form_valid(self, form):
        """
            Grava a data avaliação do responsável
        """
        avaliacao = form.save()
        avaliacao.dt_avaliacao_responsavel = datetime.now()
        # print(avaliacao.dt_avaliacao_responsavel)
        avaliacao.save()
        return super(MinhaAvaliacaoResponsavelUpdateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Seu parecer como avaliador responsável foi enviado com sucesso!')
        return reverse(self.success_url)


class MinhaAvaliacaoSuplenteUpdateView(LoginRequiredMixin, ProfessorRequiredMixin, UpdateView):
    model = Avaliacao
    form_class = MinhaAvaliacaoSuplenteForm
    template_name = 'appprofessor/minha_avaliacao_suplente_form.html'
    success_url = 'appprofessor_minha_avaliacao_list'

    def get_object(self, queryset=None):
        """
        Não deixa entrar no formulário de avaliação se ele não foi designado como 
        avaliador suplente
        """
        pk = self.kwargs.get('pk')
        try:
            obj = Avaliacao.objects.get(pk=pk, avaliador_suplente=self.request.user)
        except:
            raise Http404("Você não foi designado como avaliador suplente para esta submissão")
        return obj

    def form_valid(self, form):
        """
            Grava a data avaliação do suplente
        """
        avaliacao = form.save()
        avaliacao.dt_avaliacao_suplente = datetime.now()
        avaliacao.save()
        return super(MinhaAvaliacaoSuplenteUpdateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, 'Seu parecer como avaliador suplente foi enviado com sucesso!')
        return reverse(self.success_url)
    
    
class DocumentoListView(LoginRequiredMixin, ProfessorRequiredMixin, ListView):
    model = Documento
    template_name = 'appprofessor/documento_list.html'
    
    def get_queryset(self):
        queryset = super(DocumentoListView, self).get_queryset()
        return queryset.filter(Q(is_active = True)) 