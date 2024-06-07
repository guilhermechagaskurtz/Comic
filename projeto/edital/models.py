from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from submissao.models import Submissao
from avaliacao.models import Avaliacao

class EditalAtivoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(encerra__gte = datetime.now())


class Edital(models.Model):

    numero = models.CharField(_(u'Número do Edital *'), max_length=20, help_text='Campo obrigatório como todos os que tiverem *')
    descricao = models.CharField(_(u'Descrição *'), max_length=200)
    abertura = models.DateField(_(u'Abertura do edital *'), blank = False , null = False, help_text='dd/mm/aaaa')
    encerra = models.DateField(_(u'Encerramento do edital * '), blank = False , null = False, help_text='dd/mm/aaaa')

    objects = models.Manager()
    edital_vigente = EditalAtivoManager()

    class Meta:
        ordering = ['numero', 'abertura']

    def __str__(self):
        return '%s - Fim: %s' % (self.numero, self.encerra.strftime('%d/%m/%Y'))

    def save(self, *args, **kwargs):
        self.descricao = self.descricao.upper()
        self.numero = self.numero.upper()
        super(Edital, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('edital_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('edital_delete', args=[str(self.id)])

    @property
    def get_submissoes_todas_list_url(self):
        return reverse('submissao_edital_list', kwargs={'pk_edital': self.pk, 'situacao': 'TODAS'})

    @property
    def get_submissoes_aprovadas_list_url(self):
        return reverse('submissao_edital_list', kwargs={'pk_edital': self.pk, 'situacao':'APROVADAS'})

    @property
    def get_submissoes_reprovadas_list_url(self):
        return reverse('submissao_edital_list', kwargs={'pk_edital': self.pk, 'situacao': 'REPROVADAS'})

    @property
    def submissoes(self):
        return Submissao.objects.filter(edital=self)

    @property
    def submissoes_aprovadas(self):
        return self.submissoes.filter(id__in=[avaliacao.submissao.id for avaliacao in Avaliacao.objects.filter(status='APROVADO', submissao__edital=self)])

    @property
    def submissoes_reprovadas(self):
        return self.submissoes.filter(id__in=[avaliacao.submissao.id for avaliacao in
                                              Avaliacao.objects.filter(status='REPROVADO', submissao__edital=self)])