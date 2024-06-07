# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

# Create your models here.
class Instituicao(models.Model):
    nome = models.CharField(_(u'Nome *'), max_length=100, help_text='Campo obrigatório como todos os que tiverem *')
    sigla = models.CharField('Sigla *', max_length=20)
    site = models.CharField(_(u'Site instituição *'),max_length=100)
    contato = models.CharField(_(u'Nome completo do contato'),max_length=100,blank=True)
    email = models.EmailField(_(u'Email do contato'),max_length=100,blank=True)
    telefone = models.CharField(_(u'Telefone do contato'),max_length=100,blank=True)
    class Meta:
        ordering = ['sigla']

    def __str__(self):
        return '%s - %s ' % (self.sigla, self.nome)

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        self.sigla = self.sigla.upper()
        super(Instituicao, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('instituicao_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('instituicao_delete', args=[str(self.id)])