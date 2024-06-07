from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from datetime import datetime

from avaliacao.models import Avaliacao
from edital.models import Edital
from submissao.models import Submissao
from usuario.models import Usuario


class SubmissaoForm(forms.ModelForm):
    # responsavel = forms.ModelChoiceField(label='Responsável pelo projeto (orientador) *', queryset=Usuario.professores.all())
    colaborador = forms.ModelMultipleChoiceField(label='Colaboradores (co-orientadores)', queryset=Usuario.professores.all(),
                                         required=False, help_text='Para selecionar ou deselecionar um colaborador pressione CTRL + Botão Esquerdo do mouse ou Command + Botão Esquerdo do mouse')
    edital = forms.ModelChoiceField(label='Edital', queryset=Edital.edital_vigente)
    
    
    class Meta:
        model = Submissao
        fields = ['edital', 'colaborador', 'local_execucao' , 'area', 'curso_graduacao_vinculado', 
                  'curso_pos_graduacao', 'grupo_pesquisa',  'titulo', 'resumo', 'palavras_chave', 
                  'instituicoes_parceiras', 'arquivo_projeto']

    def clean_colaborador(self):
        colaborador = self.cleaned_data.get('colaborador')
        responsavel = self.cleaned_data.get('responsavel')

        if (responsavel in colaborador.all()):
            raise forms.ValidationError('Um professor não pode ser ao mesmo tempo responsável e colaborador')
        return colaborador

class MinhaAvaliacaoResponsavelForm(forms.ModelForm):
    TIPOS_RESPOSTAS = (
        ('',''),
        ('SIM', 'Sim'),
        ('NÃO', 'Não' ),
        ('EM PARTE', 'Em parte'),
        ('NÃO SE APLICA', 'Não se aplica'),
    )
    tem_introducao_responsavel = forms.ChoiceField(label='A introdução está adequada?', choices=TIPOS_RESPOSTAS)
    tem_justificativa_responsavel = forms.ChoiceField(label='Existe uma justificativa coerente?',choices=TIPOS_RESPOSTAS)
    tem_objetivos_responsavel = forms.ChoiceField(label='Os objetivos são claros e exequíveis?',choices=TIPOS_RESPOSTAS)
    tem_metodologia_desenho_estudo_responsavel = forms.ChoiceField(label='Metodologicamente, o desenho do estudo está claramente definido?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_local_estudo_responsavel = forms.ChoiceField(label='Metodologicamente, o local de realização do estudo e a população estão claramente definidos?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_amostra_estudo_responsavel = forms.ChoiceField(label='Metodologicamente, há definição da amostra para estudos quantitativos?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_inclusao_estudo_responsavel = forms.ChoiceField(label='Metodologicamente, os critérios de inclusão e/ou exclusão estão claros?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_coleta_estudo_responsavel = forms.ChoiceField(label='Metodologicamente, o período de coleta de dados está definido?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_coleta_instrumento_estudo_responsavel = forms.ChoiceField(label='Metodologicamente, o projeto inclui um instrumento de coleta de dados em apêndice?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_etica_estudo_responsavel = forms.ChoiceField(label='Metodologicamente, os aspectos éticos estão descritos?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_riscos_estudo_responsavel = forms.ChoiceField(label='Metodologicamente, os riscos do estudo estão descritos?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_assentimento_estudo_responsavel = forms.ChoiceField(label='Metodologicamente, apresenta termo de assentimento em apêndice?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_consentimento_estudo_responsavel = forms.ChoiceField(label='Metodologicamente, apresenta termo de consentimento livre e esclarecido em apêndice?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_confidencialidade_estudo_responsavel = forms.ChoiceField(label='Metodologicamente, apresenta termo de confidencialidade?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_exequivel_estudo_responsavel = forms.ChoiceField(label='Metodologicamente, o projeto é exequível na instituição/unidade definido?', choices=TIPOS_RESPOSTAS)
    tem_cronograma_responsavel = forms.ChoiceField(label='Há um cronograma de atividades?', choices=TIPOS_RESPOSTAS)
    tem_orcamento_responsavel = forms.ChoiceField(label='Projeto possui orçamento?', choices=TIPOS_RESPOSTAS)
    tem_orcamento_agencia_responsavel = forms.ChoiceField(label='O orçamento é de agência de fomento?', choices=TIPOS_RESPOSTAS)
    tem_referencias_responsavel = forms.ChoiceField(label='Há referências bibliográficas no projeto?', choices=TIPOS_RESPOSTAS)
    tem_relevancia_responsavel = forms.ChoiceField(label='O projeto tem relevância para a instituição envolvida?', choices=TIPOS_RESPOSTAS)
    tem_assitencia_responsavel = forms.ChoiceField(label='O projeto interfere na rotina ou prática assistencial vigente de modo significativo?', choices=TIPOS_RESPOSTAS)
    tem_relevancia_responsavel = forms.ChoiceField(label='O projeto tem relevância para a instituição envolvida?', choices=TIPOS_RESPOSTAS)
    tem_mudanca_responsavel = forms.ChoiceField(label='O projeto prevê mudanças de alguma prática institucional vigente?', choices=TIPOS_RESPOSTAS)
    tem_nova_pratica_assistencial_responsavel = forms.ChoiceField(label='O projeto prevê implementação de nova prática assistencial?', choices=TIPOS_RESPOSTAS)
    tem_produto_responsavel = forms.ChoiceField(label='O projeto prevê desenvolvimento de produto ou tecnologia leve-dura ou dura?', choices=TIPOS_RESPOSTAS)

    class Meta:
        model = Avaliacao
        fields = ['tem_introducao_responsavel', 'tem_objetivos_responsavel',
                    'tem_justificativa_responsavel', 'tem_metodologia_desenho_estudo_responsavel',
                    'tem_metodologia_local_estudo_responsavel',
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
                    'tem_relevancia_responsavel',
                    'tem_mudanca_responsavel',
                    'tem_nova_pratica_assistencial_responsavel',
                    'tem_produto_responsavel',
                    'parecer_avaliador_responsavel']


class MinhaAvaliacaoSuplenteForm(forms.ModelForm):
    TIPOS_RESPOSTAS = (
        ('', ''),
        ('SIM', 'Sim'),
        ('NÃO', 'Não'),
        ('EM PARTE', 'Em parte'),
        ('NÃO SE APLICA', 'Não se aplica'),
    )
    tem_introducao_suplente = forms.ChoiceField(label='A introdução está adequada?', choices=TIPOS_RESPOSTAS)
    tem_justificativa_suplente = forms.ChoiceField(label='Existe uma justificativa coerente?',choices=TIPOS_RESPOSTAS)
    tem_objetivos_suplente = forms.ChoiceField(label='Os objetivos são claros e exequíveis?',choices=TIPOS_RESPOSTAS)
    tem_metodologia_desenho_estudo_suplente = forms.ChoiceField(label='Metodologicamente, o desenho do estudo está claramente definido?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_local_estudo_suplente = forms.ChoiceField(label='Metodologicamente, o local de realização do estudo e a população estão claramente definidos?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_amostra_estudo_suplente = forms.ChoiceField(label='Metodologicamente, há definição da amostra para estudos quantitativos?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_inclusao_estudo_suplente = forms.ChoiceField(label='Metodologicamente, os critérios de inclusão e/ou exclusão estão claros?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_coleta_estudo_suplente = forms.ChoiceField(label='Metodologicamente, o período de coleta de dados está definido?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_coleta_instrumento_estudo_suplente = forms.ChoiceField(label='Metodologicamente, o projeto inclui um instrumento de coleta de dados em apêndice?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_etica_estudo_suplente = forms.ChoiceField(label='Metodologicamente, os aspectos éticos estão descritos?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_riscos_estudo_suplente = forms.ChoiceField(label='Metodologicamente, os riscos do estudo estão descritos?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_assentimento_estudo_suplente = forms.ChoiceField(label='Metodologicamente, apresenta termo de assentimento em apêndice?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_consentimento_estudo_suplente = forms.ChoiceField(label='Metodologicamente, apresenta termo de consentimento livre e esclarecido em apêndice?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_confidencialidade_estudo_suplente = forms.ChoiceField(label='Metodologicamente, apresenta termo de confidencialidade?', choices=TIPOS_RESPOSTAS)
    tem_metodologia_exequivel_estudo_suplente = forms.ChoiceField(label='Metodologicamente, o projeto é exequível na instituição/unidade definido?', choices=TIPOS_RESPOSTAS)
    tem_cronograma_suplente = forms.ChoiceField(label='Há um cronograma de atividades?', choices=TIPOS_RESPOSTAS)
    tem_orcamento_suplente = forms.ChoiceField(label='Projeto possui orçamento?', choices=TIPOS_RESPOSTAS)
    tem_orcamento_agencia_suplente = forms.ChoiceField(label='O orçamento é de agência de fomento?', choices=TIPOS_RESPOSTAS)
    tem_referencias_suplente = forms.ChoiceField(label='Há referências bibliográficas no projeto?', choices=TIPOS_RESPOSTAS)
    tem_relevancia_suplente = forms.ChoiceField(label='O projeto tem relevância para a instituição envolvida?', choices=TIPOS_RESPOSTAS)
    tem_assitencia_suplente = forms.ChoiceField(label='O projeto interfere na rotina ou prática assistencial vigente de modo significativo?', choices=TIPOS_RESPOSTAS)
    tem_relevancia_suplente = forms.ChoiceField(label='O projeto tem relevância para a instituição envolvida?', choices=TIPOS_RESPOSTAS)
    tem_mudanca_suplente = forms.ChoiceField(label='O projeto prevê mudanças de alguma prática institucional vigente?', choices=TIPOS_RESPOSTAS)
    tem_nova_pratica_assistencial_suplente = forms.ChoiceField(label='O projeto prevê implementação de nova prática assistencial?', choices=TIPOS_RESPOSTAS)
    tem_produto_suplente = forms.ChoiceField(label='O projeto prevê desenvolvimento de produto ou tecnologia leve-dura ou dura?', choices=TIPOS_RESPOSTAS)

    class Meta:
        model = Avaliacao
        fields = ['tem_introducao_suplente','tem_objetivos_suplente',
                    'tem_justificativa_suplente','tem_metodologia_desenho_estudo_suplente',
                    'tem_metodologia_local_estudo_suplente',
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
                    'tem_relevancia_suplente',
                    'tem_mudanca_suplente',
                    'tem_nova_pratica_assistencial_suplente',
                    'tem_produto_suplente',
                    'parecer_avaliador_suplente']
              
              
class BuscaSubmissaoForm(forms.Form):
    TIPOS_STATUS = (
        (None,'-------------'),
        ('APROVADO', 'Aprovado'),
        ('EM ANÁLISE', 'Em Análise' ),
        ('PENDENTE', 'Pendente'),
        ('PÓS CORREÇÃO', 'Pós correção' ),
        ('REPROVADO', 'Reprovado' ),
        ('TRANCADO', 'Trancado'),
    )

    edital = forms.ModelChoiceField(label='Edital', queryset=Edital.objects.all(), required=False)
    titulo = forms.CharField(label='Título ou parte', required=False)
    status = forms.ChoiceField(label='Status', choices=TIPOS_STATUS, required=False)
    nome_integrante = forms.CharField(label='Nome colaborador ou parte', required=False)
    
    
    
class BuscaAvaliacaoForm(forms.Form):
    edital = forms.ModelChoiceField(label='Edital', queryset=Edital.objects.all(), required=False)
    titulo = forms.CharField(label='Título ou parte dele', required=False)
    nome_integrante = forms.CharField(label='Nome pesquisador ou parte dele', required=False)