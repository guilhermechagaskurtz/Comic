from django import forms
from avaliacao.models import Avaliacao
from edital.models import Edital

class BuscaComissaoForm(forms.Form):
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