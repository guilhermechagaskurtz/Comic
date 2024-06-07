from django import forms
from django.db import models

from edital.models import Edital
from usuario.models import Usuario

from .models import Avaliacao


class AvaliacaoForm(forms.ModelForm):
    avaliador_responsavel = forms.ModelChoiceField(label='Selecione um professor como avaliador responsável *', queryset=Usuario.professores.all())
    avaliador_suplente = forms.ModelChoiceField(label='Selecione um professor como avaliador suplente', queryset=Usuario.professores.all(), required=False)

    
    class Meta:
        model = Avaliacao
        fields = ['submissao', 'avaliador_responsavel', 'avaliador_suplente','dt_limite_avaliacao', 
	'tem_introducao_responsavel','tem_objetivos_responsavel',
    'tem_justificativa_responsavel','tem_metodologia_desenho_estudo_responsavel','tem_metodologia_local_estudo_responsavel',
    'tem_metodologia_amostra_estudo_responsavel',
    'tem_metodologia_inclusao_estudo_responsavel',
    'tem_metodologia_coleta_estudo_responsavel',
    'tem_metodologia_coleta_instrumento_estudo_responsavel',
    'tem_metodologia_etica_estudo_responsavel',
    'tem_metodologia_riscos_estudo_responsavel',
    'tem_metodologia_assentimento_estudo_responsavel',
    'tem_metodologia_consentimento_estudo_responsavel',
    'tem_metodologia_confidencialidade_estudo_responsavel',
    'tem_metodologia_exequivel_estudo_responsavel',
    'tem_cronograma_responsavel',
    'tem_orcamento_responsavel',
    'tem_orcamento_agencia_responsavel',
    'tem_referencias_responsavel',
    'tem_relevancia_responsavel',
    'tem_assitencia_responsavel',
    'tem_mudanca_responsavel',
    'tem_nova_pratica_assistencial_responsavel',
    'tem_produto_responsavel',
	'parecer_avaliador_responsavel',
	'tem_introducao_suplente','tem_objetivos_suplente',
    'tem_justificativa_suplente','tem_metodologia_desenho_estudo_suplente','tem_metodologia_local_estudo_suplente',
    'tem_metodologia_amostra_estudo_suplente',
    'tem_metodologia_inclusao_estudo_suplente',
    'tem_metodologia_coleta_estudo_suplente',
    'tem_metodologia_coleta_instrumento_estudo_suplente',
    'tem_metodologia_etica_estudo_suplente',
    'tem_metodologia_riscos_estudo_suplente',
    'tem_metodologia_assentimento_estudo_suplente',
    'tem_metodologia_consentimento_estudo_suplente',
    'tem_metodologia_confidencialidade_estudo_suplente',
    'tem_metodologia_exequivel_estudo_suplente',
    'tem_cronograma_suplente',
    'tem_orcamento_suplente',
    'tem_orcamento_agencia_suplente',
    'tem_referencias_suplente',
    'tem_relevancia_suplente',
    'tem_assitencia_suplente',
    'tem_mudanca_suplente',
    'tem_nova_pratica_assistencial_suplente',
    'tem_produto_suplente',
    'parecer_avaliador_suplente']
    
    success_url = 'avaliacao_list'
            
    def clean_avaliador_suplente(self):
        avaliador_responsavel = self.cleaned_data.get('avaliador_responsavel')
        avaliador_suplente = self.cleaned_data.get('avaliador_suplente')
        submissao = self.cleaned_data.get('submissao')

        if avaliador_responsavel:
            if (avaliador_suplente == avaliador_responsavel):
                raise forms.ValidationError('Um professor não pode ser ao mesmo tempo avaliador responsável e avaliador suplente')

            if (avaliador_suplente == submissao.responsavel or avaliador_suplente in submissao.colaborador.all()):
                raise forms.ValidationError('Um professor não pode ser ao mesmo tempo avaliador e integrante de um projeto')

        return avaliador_suplente

    def clean_avaliador_responsavel(self):
        avaliador_responsavel = self.cleaned_data.get('avaliador_responsavel')        
        submissao = self.cleaned_data.get('submissao')
        
        if (avaliador_responsavel == submissao.responsavel or avaliador_responsavel in submissao.colaborador.all()):
            raise forms.ValidationError('Um professor não pode ser ao mesmo tempo avaliador e integrante de um projeto')

        return avaliador_responsavel


class BuscaAvaliacaoForm(forms.Form):
    TIPOS_STATUS = (
        (None,'-------------'),
        ('APROVADO', 'Aprovado'),
        ('EM ANÁLISE', 'Em Análise' ),
        ('PENDENTE', 'Pendente'),
        ('PÓS CORREÇÃO', 'Pós Correção' ),
        ('REPROVADO', 'Reprovado' ),
        ('TRANCADO', 'Trancado'),
    )

    edital = forms.ModelChoiceField(label='Edital', queryset=Edital.objects.all(), required=False)
    titulo = forms.CharField(label='Título ou parte dele', required=False)
    status = forms.ChoiceField(label='Status do projeto', choices=TIPOS_STATUS, required=False)
    nome_integrante = forms.CharField(label='Nome pesquisador ou parte dele', required=False)