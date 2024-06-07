from django import forms

from edital.models import Edital
from usuario.models import Usuario

from .models import Submissao


class SubmissaoForm(forms.ModelForm):
    responsavel = forms.ModelChoiceField(label='Responsável pelo projeto (orientador) *', queryset=Usuario.professores.all())
    colaborador = forms.ModelMultipleChoiceField(label='Colaboradores (co-orientadores)', queryset=Usuario.professores.all(),
                                         required=False, help_text='Para selecionar ou deselecionar um colaborador pressione CTRL + Botão Esquerdo do mouse ou Command + Botão Esquerdo do mouse')
    
    
    class Meta:
        model = Submissao
        fields = ['edital', 'responsavel', 'colaborador', 'local_execucao' , 'area', 
                  'curso_graduacao_vinculado', 'curso_pos_graduacao', 'grupo_pesquisa',  
                  'titulo', 'resumo', 'palavras_chave', 'instituicoes_parceiras', 
                  'arquivo_projeto']


    def clean_colaborador(self):
        colaborador = self.cleaned_data.get('colaborador')
        responsavel = self.cleaned_data.get('responsavel')

        if (responsavel in colaborador.all()):
            raise forms.ValidationError('Um professor não pode ser ao mesmo tempo responsável e colaborador')
        return colaborador
            

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
    titulo = forms.CharField(label='Título ou parte dele', required=False)
    status = forms.ChoiceField(label='Status do projeto', choices=TIPOS_STATUS, required=False)
    nome_integrante = forms.CharField(label='Nome pesquisador ou parte dele', required=False)