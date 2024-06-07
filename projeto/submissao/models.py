from __future__ import unicode_literals

import os

from datetime import datetime

from django.conf import settings
from django.contrib import messages
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from usuario.models import Usuario
from comissao.models import Comissao
from avaliacao.models import Avaliacao


class Submissao(models.Model):
    #1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPOS = (
        ('CIÊNCIAS DA SAÚDE', 'Ciências da Saúde'),
        ('CIÊNCIAS HUMANAS', 'Ciências Humanas' ),
        ('CIÊNCIAS SOCIAIS', 'Ciências Sociais'),
        ('CIÊNCIAS TECNOLÓGICAS', 'Ciências Tecnológicas' ),
    )
    
    edital = models.ForeignKey('edital.Edital', verbose_name='Edital vigente *', null=False, blank=False, on_delete=models.PROTECT, help_text='Campo obrigatório como todos os que tiverem *')
    responsavel = models.ForeignKey('usuario.Usuario', verbose_name='Responsável pelo projeto *', related_name='responsavel', null=False, blank=False, on_delete=models.PROTECT, help_text='Você deve selecionar o professor responsável')
    colaborador = models.ManyToManyField('usuario.Usuario', verbose_name='Colaborador(es)', null=True, blank=True, related_name='colaborador', help_text='Para selecionar ou deselecionar um colaborador pressione CTRL + Botão Esquerdo do mouse ou Command + Botão Esquerdo do mouse')
    local_execucao = models.CharField(_(u'Nome da instituição de execução do projeto *'),max_length=150, help_text='Campo obrigatório como todos os que tiverem *')
    area = models.CharField(_(u'Área de ensino, pesquisa e extensão de execução do projeto *'), max_length=25, choices=TIPOS)
    curso_graduacao_vinculado = models.CharField(_('Curso(s) de graduação vinculado(s) *'),null=False,blank=False,help_text='Nome dos cursos associados ao projeto separados por ponto-e-vírgula',max_length=100)
    curso_pos_graduacao = models.CharField(_('Curso(s) de pós-graduação vinculado(s)'),null=True,blank=True,max_length=100, help_text='Nome dos cursos associados ao projeto separados por ponto-e-vírgula')
    grupo_pesquisa = models.CharField(_('Grupo de pesquisa vinculado'),null=True,blank=True,max_length=50, help_text='Caso esteja vinculado ao projeto')
    titulo = models.TextField(_(u'Título do projeto (200 caracteres) *'), max_length=200, null=False, blank=False)
    resumo = models.TextField(_(u'Resumo do projeto (2000 caracteres) *'),max_length=2000, null=False,blank=False)
    palavras_chave = models.TextField(_(u'Palavras-chave: 3 a 5 expressões separadas por ponto-e-vírgula *'), max_length=100, null=False, blank=False)
    instituicoes_parceiras = models.ManyToManyField('instituicao.Instituicao', verbose_name='Instituições parceiras', null=True, blank=True, help_text='Para selecionar ou deselecionar uma instituição parceira pressione CTRL + Botão Esquerdo do mouse ou Command + Botão Esquerdo do mouse')
    
    arquivo_projeto = models.FileField(_(u'Arquivo do projeto *'), upload_to='midias', help_text='Use arquivo .pdf para enviar seu projeto')
    arquivo_atualizacao_pendencia_projeto = models.FileField(_(u'Arquivo da atualização de pendência do projeto (Use arquivo .pdf para enviar seu projeto)'), upload_to='midias', null=True, blank=True, help_text='ATENÇÃO: Depois de GRAVAR não será possível alterar!!')
    
    arquivo_comite_etica = models.FileField(_('Arquivo do parecer consubstanciado do CEP'), null=True, blank=True, upload_to='midias', help_text='Use arquivo .pdf para enviar a carta do Comitê de Ética')
    arquivo_relatorio_parcial = models.FileField(_('Arquivo do relatório parcial das atividades do projeto. DEVE ser atualizado com frequência'), null=True, blank=True, upload_to='midias', help_text='Use arquivo .pdf para enviar o relatório parcial')
    arquivo_relatorio_final = models.FileField(_('Arquivo relatório final e devolutiva do projeto'), null=True, blank=True, upload_to='midias', help_text='Use arquivo .pdf para enviar o relatório final')
    
    arquivo_emenda1 = models.FileField(_('Arquivo para PRIMEIRA emenda'), null=True, blank=True, upload_to='midias', help_text='Use arquivo .pdf para enviar a emenda')
    arquivo_emenda2 = models.FileField(_('Arquivo para SEGUNDA emenda'), null=True, blank=True, upload_to='midias', help_text='Use arquivo .pdf para enviar a emenda')
    arquivo_emenda3 = models.FileField(_('Arquivo para TERCEIRA emenda'), null=True, blank=True, upload_to='midias', help_text='Use arquivo .pdf para enviar a emenda')
    
    registros_apos_aprovacao = models.TextField(_('Registros e observações no projeto após aprovação'), max_length=5000, null=True, blank=True, help_text='Use sempre este espaço se precisar registrar alguma alteração ou ponderar sobre algo')
    
    dt_atualizacao_submissao = models.DateTimeField(_('Data que o projeto foi atualizado'), blank=True, null=True)
    dt_cadastro_submissao = models.DateTimeField(_('Data que o projeto foi enviado'), auto_now_add=True)
    
    class Meta:
        ordering = ['-edital__encerra', '-avaliacao__comissao__status', 'dt_cadastro_submissao','titulo']

    def __str__(self):
        colaboradores = ''
        for c in self.colaborador.all():
            colaboradores += c.nome + ', '
        return '%s - %s - %s' % (self.titulo_curto, self.responsavel, colaboradores)
    
    def save(self, *args, **kwargs):
        #para a submissão create não funciona por que precisa salvar o ID da submissão
        #antes de pegar os colaboradores
        #exemplo: id_sub: none , id_colab: 2
                  #id_sub:none , id_colab: 1
        
        #Para a submissão update funciona por que já tem o ID da submissão
        #exemplo: id_sub: 1 , id_colab: 2
                  #id_sub:1 , id_colab: 1
        #colab = self.colaborador.all()
        
        self.local_execucao = self.local_execucao.upper()
        self.titulo = self.titulo.upper()
        self.curso_graduacao_vinculado = self.curso_graduacao_vinculado.upper()
       
        """ Identifica se um arquivo atualizacao_pendencia do projeto foi enviado
            e entao altera o status da avaliacao desta submissao para 'PÓS CORREÇÃO'
            para a comissao reavaliar agora com o novo arquivo"""
        if self.id:
            #no update
            submissao_pos_tratamento_pendencia = Submissao.objects.get(id=self.id)
            try:
                #se a submissao estiver aprovada, não entra em pos-correcao
                if submissao_pos_tratamento_pendencia:
                    if submissao_pos_tratamento_pendencia.avaliacao:
                        if submissao_pos_tratamento_pendencia.avaliacao.comissao:
                            if submissao_pos_tratamento_pendencia.avaliacao.comissao.status != 'APROVADO' and self.arquivo_atualizacao_pendencia_projeto:
                                Comissao.objects.filter(avaliacao_comissao__submissao=self).update(status='PÓS CORREÇÃO')
            except:
                pass
        else:
            self.dt_atualizacao_submissao = datetime.now() #grava a data de atualização também no insert, para dados legados
     
        super(Submissao, self).save(*args, **kwargs)

    @property
    def permite_alterar(self):
        return timezone.now().date() < self.edital.encerra and (not Avaliacao.objects.filter(submissao=self) or self.avaliacao.comissao.status == "EM EDIÇÃO")


    @property 
    def permite_corrigir(self):
        return 'PENDENTE' == self.avaliacao.comissao.status
    
    @property
    def get_parecer_comissao(self):
        return Comissao.objects.filter(avaliacao_comissao__submissao=self)

    @property
    def get_absolute_url(self):
        return reverse('submissao_update', args=[str(self.id)])

    @property
    def get_absolute_url_pendente(self):
        return reverse('submissao_pendente_update', args=[str(self.id)])

    @property
    def get_absolute_url_aprovado(self):
        return reverse('submissao_aprovado_update', args=[str(self.id)])

    @property
    def get_approfessor_absolute_url(self):
        return reverse('appprofessor_submissao_update', args=[str(self.id)])
    
    @property
    def get_approfessor_absolute_url_pendente(self):
        return reverse('appprofessor_submissao_pendente_update', args=[str(self.id)])
    
    @property
    def get_approfessor_absolute_url_aprovado(self):
        return reverse('appprofessor_submissao_aprovado_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('submissao_delete', args=[str(self.id)])

    @property
    def get_delete_appprofessor_url(self):
        return reverse('appprofessor_submissao_delete', args=[str(self.id)])
    
    @property
    def get_avaliacao(self):
        try:
            return Avaliacao.objects.get(submissao=self)
        except:
            return None

    @property
    def get_avaliacao_create_update_url(self):
        """
            Se existe uma avaliacao para esta submissao,
            retornar a url de edicao desta avaliacao
            caso contrario, envia para a tela de criacao
            de uma avaliacao, passando o id da submissao como
            parametro GET
        """
        try:
            return self.get_avaliacao.get_absolute_url
        except:
            return '%s?submissao_id=%d' % (reverse('avaliacao_create'), self.id)

    @property
    def titulo_curto(self):
        return self.titulo[0:80].strip()

    @property
    def get_primeiro_arquivo_parecer_comissao(self):
        objetos = Comissao.objects.filter(avaliacao_comissao__submissao=self)
        if (objetos):
            return objetos[0].arquivo_parecer_comissao
        return None
        
    @property
    def get_segundo_arquivo_parecer_comissao(self):
        objetos = Comissao.objects.filter(avaliacao_comissao__submissao=self)
        if (objetos):
            return objetos[0].arquivo_parecer_comissao_pendencia
        return None


#triggers para limpeza dos arquivos apagados ou alterados. No Django é chamado de signals
#deleta os arquivo fisico ao excluir o item midia
@receiver(models.signals.post_delete, sender=Submissao)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.arquivo_projeto:
        if os.path.isfile(instance.arquivo_projeto.path):
            os.remove(instance.arquivo_projeto.path)

#deleta o arquivo fisico ao alterar o arquivo do item midia
@receiver(models.signals.pre_save, sender=Submissao)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        obj = Submissao.objects.get(pk=instance.pk)

        if not obj.arquivo_projeto:
            return False

        old_file = obj.arquivo_projeto
    except Submissao.DoesNotExist:
        return False

    new_file = instance.arquivo_projeto
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
