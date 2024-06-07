from __future__ import unicode_literals

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models import signals
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from django.contrib import messages
from mail_templated import EmailMessage

from utils.gerador_hash import gerar_hash

# import os

class Comissao(models.Model):    
	#1 campo da tupla fica no banco de dados
    #2 campo da tupla eh mostrado para o usuario
    TIPOS_STATUS = (
        ('APROVADO', 'Aprovado'),
        ('EM ANÁLISE', 'Em Análise' ),
        ('EM EDIÇÃO', 'Em Edição' ),
        ('PÓS CORREÇÃO', 'Pós Correção' ),
        ('PENDENTE', 'Pendente'),
        ('REPROVADO', 'Reprovado' ),
        ('TRANCADO', 'Trancado'),
        ('RETIRADO PELO PROFESSOR', 'Retirado pelo professor'),
        ('RETIRADO PELO COMIC', 'Retirado pelo COMIC'),
    ) 
    
    avaliacao_comissao = models.OneToOneField('avaliacao.Avaliacao', verbose_name= 'Selecione uma avaliação de projeto submetido para parecer da comissão *', null=False, blank=False, on_delete=models.PROTECT)
    # avaliacao_comissao = models.ForeignKey('avaliacao.Avaliacao', verbose_name= 'Selecione uma avaliação para parecer da comissão *', null=False, blank=False, on_delete=models.PROTECT)
    status = models.CharField(_(u'Status final do projeto *'), max_length=25, default='EM ANÁLISE', choices=TIPOS_STATUS)
    dt_avaliacao_comissao = models.DateTimeField(_('Data da avaliação da comissão'), blank=True, null=True)
    arquivo_parecer_comissao = models.FileField(_(u'Arquivo inicial de resposta à submissão do projeto  (Use arquivo .pdf para enviar seu projeto) *'), blank=True, null=True, upload_to='midias', help_text='Use arquivo .pdf para a resposta')
    arquivo_parecer_comissao_pendencia = models.FileField(_(u'Arquivo de parecer depois das correções solicitadas pela comissão  (Use arquivo .pdf para enviar seu projeto)'), blank=True, null=True, upload_to='midias', help_text='Use arquivo .pdf para a resposta')
    comentario = models.TextField(_('Comentários'), blank=True, null=True, help_text='Digite todo e qualquer comentário ou anotação pertinente')
    dt_trancado = models.DateField(_('Data de trancamento do projeto'), blank=True, null=True)
    slug = models.SlugField('Hash',max_length= 200,null=True,blank=True)
    
    class Meta:
        ordering = ['-status','dt_avaliacao_comissao','avaliacao_comissao'] 

    def __str__(self):
        return '%s' % (self.avaliacao_comissao)
    
    def email_troca_status(self):
        if self.id:
            objeto_comissao_teste = Comissao.objects.get(id=self.id)
            if objeto_comissao_teste.status != self.status:
                try:
                    """ enviar e-mail para avisar """
                    message = EmailMessage('usuario/email/troca_status.html', {'usuario': self.avaliacao_comissao.submissao.responsavel},
                                settings.EMAIL_HOST_USER, to=[self.avaliacao_comissao.submissao.responsavel.email])
                    message.send()
                except:
                    pass
                    # messages.warning(self, "Processo realizado com sucesso, mas houve problemas com email. Responsável não foi notificado!")
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        self.dt_trancado = timezone.now().date() if self.status == 'TRANCADO' else None
        self.email_troca_status()
        super(Comissao, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('comissao_update', args=[str(self.id)])
    
    @property
    def get_delete_url(self):
        return reverse('comissao_delete', args=[str(self.id)])