from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from utils.gerador_hash import gerar_hash


class Documento(models.Model):

    descricao_arquivo = models.CharField(_('Descrição do documento *'), unique=True, max_length=100, help_text='* Campos obrigatórios')
    arquivo = models.FileField(_('Arquivo do documento'), upload_to='midias', help_text='Use arquivo .pdf para o documento')
    is_active = models.BooleanField(_('Ativo'), default=True, help_text='Se ativo, o documento pode ser usado no sistema')
    slug = models.SlugField('Hash',max_length= 200, null=True, blank=True)

    
    class Meta:
        ordering            =   ['-is_active','descricao_arquivo']
        verbose_name        =   _('documento')
        verbose_name_plural =   _('documentos')

    def __str__(self):
        return self.descricao_arquivo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = gerar_hash()
        self.descricao_arquivo = self.descricao_arquivo.upper()
        super(Documento, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('documento_update', args=[str(self.id)])

    @property
    def get_delete_url(self):
        return reverse('documento_delete', args=[str(self.id)])
