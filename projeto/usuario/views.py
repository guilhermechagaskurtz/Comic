from django.views.generic import ListView, TemplateView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib import messages
from django.urls import reverse
from django.conf import settings

from mail_templated import EmailMessage

from utils.decorators import LoginRequiredMixin

from .models import Usuario
from .forms import UsuarioRegisterForm, BuscaAlunoForm

class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'usuario/usuario_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET:
            #quando ja tem dado filtrando
            context['form'] = BuscaAlunoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            context['form'] = BuscaAlunoForm()
        return context

    def get_queryset(self):
        qs = Usuario.objects.all()

        if self.request.GET:
            #quando ja tem dado filtrando
            form = BuscaAlunoForm(data=self.request.GET)
        else:
            #quando acessa sem dado filtrando
            form = BuscaAlunoForm()

        if form.is_valid():
            nome = form.cleaned_data.get('nome')
            curso = form.cleaned_data.get('curso')

            if nome:
                qs = qs.filter(nome__icontains=nome)

            if curso:
                qs = qs.filter(curso_graduacao_vinculado__icontains=curso)
        return qs


class UsuarioCreateView(LoginRequiredMixin, CreateView):
    model = Usuario
    fields = ['tipo', 'nome', 'email','area_conhecimento_cnpq','curso_graduacao_vinculado','curso_pos_graduacao','grupo_pesquisa','data_nasc', 'cpf','rg' ,'matricula', 'lattes', 'instituicao', 'password', 'is_active']
    success_url = 'usuario_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Usuário cadastrados com sucesso!')
        return reverse(self.success_url)


class UsuarioRegisterView(CreateView):
    model = Usuario
    form_class = UsuarioRegisterForm
    template_name = 'usuario/usuario_register_form.html'
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()
        return super(UsuarioRegisterView, self).form_valid(form)
    
    def get_success_url(self):
        try:
            message = EmailMessage('usuario/email/validacao_email.html', {'usuario': self.object},
                                settings.EMAIL_HOST_USER, to=[self.object.email])
            message.send()
            return reverse('usuario_register_success')
        except:
            return reverse('usuario_register_success_falha_email') 
        


class UsuarioRegisterSuccessView(TemplateView):
    template_name= 'usuario/usuario_register_success.html'
    
class UsuarioRegisterSuccessFalhaEmailView(TemplateView):
    template_name= 'usuario/usuario_register_success_falha_email.html'


class UsuarioRegisterActivateView(RedirectView):
    models = Usuario

    def get_redirect_url(self, *args, **kwargs):
        self.object = Usuario.objects.get(slug=kwargs.get('slug'))
        self.object.is_active = True
        self.object.save()
        login(self.request, self.object)
        messages.success(self.request, 'Obrigado por acessar o SISGEP/COMIC. Esta é a sua área restrita de submissão e de avaliação de projetos.')
        return reverse('appprofessor_home')


class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['tipo', 'nome', 'email','area_conhecimento_cnpq','curso_graduacao_vinculado','curso_pos_graduacao','grupo_pesquisa','data_nasc', 'cpf','rg','matricula', 'lattes', 'instituicao', 'is_active']
    success_url = 'usuario_list'
    
    def get_success_url(self):
        messages.success(self.request, 'Dados de usuário atualizados com sucesso!')
        return reverse(self.success_url)


class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    success_url = 'usuario_list'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL. If the object is protected, send an error message.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(request, 'Usuário excluído com sucesso!')
        except Exception as e:
            messages.error(request, 'Há dependências ligadas à esse usuário, permissão negada!')
        return redirect(self.success_url)
             
            