# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from comissao.models import Comissao


class Avaliacao(models.Model):    
    TIPOS_RESPOSTAS = (
        ('SIM', 'Sim'),
        ('NÃO', 'Não' ),
        ('EM PARTE', 'Em parte'),
        ('NÃO SE APLICA', 'Não se aplica'),
    )

    submissao = models.OneToOneField('submissao.Submissao', verbose_name='Selecione um projeto submetido para avaliação *', null=False, blank=False, on_delete=models.PROTECT)
    # submissao = models.ForeignKey('submissao.Submissao', verbose_name='Selecione um projeto submetido para avaliação *', on_delete=models.PROTECT, help_text='Campo obrigatório como todos os que tiverem *')
    avaliador_responsavel = models.ForeignKey('usuario.Usuario', verbose_name='Selecione um professor como avaliador responsável *', related_name='avaliador_responsavel', on_delete=models.PROTECT)
    avaliador_suplente = models.ForeignKey('usuario.Usuario', verbose_name='Selecione um professor como avaliador suplente',related_name='avaliador_suplente', null=True, blank=True, on_delete=models.PROTECT)
    # status = models.CharField(_(u'Status do projeto'), max_length=25, choices=TIPOS_STATUS, default='EM ANÁLISE')
    dt_limite_avaliacao = models.DateTimeField(_('Data Limite para a avaliação *'), help_text='dd/mm/aaaa')

    #Campos de parecer avaliador responsavel
    dt_avaliacao_responsavel = models.DateTimeField(_('Data da avaliação do responsável'), blank=True, null=True)
    tem_introducao_responsavel = models.CharField(_(u'A introdução está adequada?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_justificativa_responsavel = models.CharField(_(u'Existe uma justificativa coerente?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_objetivos_responsavel = models.CharField(_(u'Os objetivos são claros e exequíveis?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_desenho_estudo_responsavel = models.CharField(_(u'Metodologicamente, o desenho do estudo está claramente definido?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_local_estudo_responsavel = models.CharField(_(u'Metodologicamente, o local de realização do estudo e a população estão claramente definidos?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_amostra_estudo_responsavel = models.CharField(_(u'Metodologicamente, há definição da amostra para estudos quantitativos?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_inclusao_estudo_responsavel = models.CharField(_(u'Metodologicamente, os critérios de inclusão e/ou exclusão estão claros?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_coleta_estudo_responsavel = models.CharField(_(u'Metodologicamente, o período de coleta de dados está definido?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_coleta_instrumento_estudo_responsavel = models.CharField(_(u'Metodologicamente, o projeto inclui um instrumento de coleta de dados em apêndice?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_etica_estudo_responsavel = models.CharField(_(u'Metodologicamente, os aspectos éticos estão descritos?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_riscos_estudo_responsavel = models.CharField(_(u'Metodologicamente, os riscos do estudo estão descritos?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_assentimento_estudo_responsavel = models.CharField(_(u'Metodologicamente, apresenta termo de assentimento em apêndice?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_consentimento_estudo_responsavel = models.CharField(_(u'Metodologicamente, apresenta termo de consentimento livre e esclarecido em apêndice?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_confidencialidade_estudo_responsavel = models.CharField(_(u'Metodologicamente, apresenta termo de confidencialidade?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_exequivel_estudo_responsavel = models.CharField(_(u'Metodologicamente, o projeto é exequível na instituição/unidade definido?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_cronograma_responsavel = models.CharField(_(u'Há um cronograma de atividades?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_orcamento_responsavel = models.CharField(_(u'Projeto possui orçamento?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_orcamento_agencia_responsavel = models.CharField(_(u'O orçamento é de agência de fomento?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_referencias_responsavel = models.CharField(_(u'Há referências bibliográficas no projeto?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_relevancia_responsavel = models.CharField(_(u'O projeto tem relevância para a instituição envolvida?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_assitencia_responsavel = models.CharField(_(u'O projeto interfere na rotina ou prática assistencial vigente de modo significativo?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_mudanca_responsavel = models.CharField(_(u'O projeto prevê mudanças de alguma prática institucional vigente?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_nova_pratica_assistencial_responsavel = models.CharField(_(u'O projeto prevê implementação de nova prática assistencial?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_produto_responsavel = models.CharField(_(u'O projeto prevê desenvolvimento de produto ou tecnologia leve-dura ou dura?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    parecer_avaliador_responsavel = models.TextField(_(u'Parecer do avaliador responsável (2000 caracteres)'), max_length=2000, null=True, blank=True)
    

    #Campos de parecer avaliador suplente
    dt_avaliacao_suplente = models.DateTimeField(_('Data da avaliação do suplente'), blank=True, null=True)
    tem_introducao_suplente = models.CharField(_(u'A introdução está adequada?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_justificativa_suplente = models.CharField(_(u'Existe uma justificativa coerente?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_objetivos_suplente = models.CharField(_(u'Os objetivos são claros e exequíveis?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_desenho_estudo_suplente = models.CharField(_(u'Metodologicamente, o desenho do estudo está claramente definido?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_local_estudo_suplente = models.CharField(_(u'Metodologicamente, o local de realização do estudo e a população estão claramente definidos?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_amostra_estudo_suplente = models.CharField(_(u'Metodologicamente, há definição da amostra para estudos quantitativos?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_inclusao_estudo_suplente = models.CharField(_(u'Metodologicamente, os critérios de inclusão e/ou exclusão estão claros?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_coleta_estudo_suplente = models.CharField(_(u'Metodologicamente, o período de coleta de dados está definido?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_coleta_instrumento_estudo_suplente = models.CharField(_(u'Metodologicamente, o projeto inclui um instrumento de coleta de dados em apêndice?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_etica_estudo_suplente = models.CharField(_(u'Metodologicamente, os aspectos éticos estão descritos?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_riscos_estudo_suplente = models.CharField(_(u'Metodologicamente, os riscos do estudo estão descritos?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_assentimento_estudo_suplente = models.CharField(_(u'Metodologicamente, apresenta termo de assentimento em apêndice?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_consentimento_estudo_suplente = models.CharField(_(u'Metodologicamente, apresenta termo de consentimento livre e esclarecido em apêndice?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_confidencialidade_estudo_suplente = models.CharField(_(u'Metodologicamente, apresenta termo de confidencialidade?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_metodologia_exequivel_estudo_suplente = models.CharField(_(u'Metodologicamente, o projeto é exequível na instituição/unidade definido?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_cronograma_suplente = models.CharField(_(u'Há um cronograma de atividades?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_orcamento_suplente = models.CharField(_(u'Projeto possui orçamento?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_orcamento_agencia_suplente = models.CharField(_(u'O orçamento é de agência de fomento?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_referencias_suplente = models.CharField(_(u'Há referências bibliográficas no projeto?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_relevancia_suplente = models.CharField(_(u'O projeto tem relevância para a instituição envolvida?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_assitencia_suplente = models.CharField(_(u'O projeto interfere na rotina ou prática assistencial vigente de modo significativo?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_mudanca_suplente = models.CharField(_(u'O projeto prevê mudanças de alguma prática institucional vigente?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_nova_pratica_assistencial_suplente = models.CharField(_(u'O projeto prevê implementação de nova prática assistencial?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    tem_produto_suplente = models.CharField(_(u'O projeto prevê desenvolvimento de produto ou tecnologia leve-dura ou dura?'), max_length=25, choices=TIPOS_RESPOSTAS, null=True, blank=True)
    parecer_avaliador_suplente = models.TextField(_(u'Parecer do avaliador suplente (2000 caracteres)'), max_length=2000, null=True, blank=True)
    
    class Meta:
        ordering = ['comissao__status', 'dt_limite_avaliacao', 'submissao'] 

    def __str__(self):
        return '%s' % (self.submissao)

    def save(self, *args, **kwargs):
        super(Avaliacao, self).save(*args, **kwargs)
    
    @property
    def get_absolute_url(self):
        return reverse('avaliacao_update', args=[str(self.id)])

    @property
    def get_avaliacao_responsavel_url(self):
        return reverse('appprofessor_minha_avaliacao_responsavel', args=[str(self.id)])

    @property
    def get_avaliacao_suplente_url(self):
        return reverse('appprofessor_minha_avaliacao_suplente', args=[str(self.id)])
    
    @property
    def get_delete_url(self):
        return reverse('avaliacao_delete', args=[str(self.id)])

    @property
    def get_parecer(self):
        try:
            return Comissao.objects.get(avaliacao_comissao=self)
        except:
            return None

    @property
    def get_parecer_create_update_url(self):
        """
            Se existe um parecer na comissão para esta avaliação,
            retornar a url de edicao deste parecer
            caso contrario, envia para a tela de criacao
            de um parecer, passando o id da avaliacao como
            parametro GET
        """
        try:
            return self.get_parecer.get_absolute_url
        except:
            return '%s?avaliacao_id=%d' % (reverse('comissao_create'), self.id)
