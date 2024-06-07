from django import forms
from .models import Usuario
from instituicao.models import Instituicao

class UsuarioRegisterForm(forms.ModelForm):
    TIPOS_REGISTER = (
        ('PROFESSOR','Professor'),
    )
    AREAS = (
        ('CIÊNCIAS DA SAÚDE', 'Ciências da Saúde'),
        ('CIÊNCIAS HUMANAS', 'Ciências Humanas' ),
        ('CIÊNCIAS SOCIAIS', 'Ciências Sociais'),
        ('CIÊNCIAS TECNOLÓGICAS', 'Ciências Tecnológicas' ),
    )
    tipo = forms.ChoiceField(label='Tipo',choices=TIPOS_REGISTER)
    nome = forms.CharField(label='Nome' , help_text='Campo obrigatório como todos os que tiverem *' )
    email = forms.EmailField(label= 'Email *', max_length=100)
    lattes = forms.CharField(label='Lattes *', help_text="Clique <a href='http://buscatextual.cnpq.br/buscatextual' target='_blank'> aqui </a> para descobrir", max_length=100, required = True)
    area_conhecimento_cnpq =  forms.ChoiceField(label='Área de conhecimento *', choices=AREAS, required = True)
    curso_graduacao_vinculado = forms.CharField(label='Curso de graduação vinculado *', help_text='Nome do curso que está lotado',max_length=50)
    instituicao = forms.ModelChoiceField(label='Instituição',queryset=Instituicao.objects.all())
    cpf = forms.CharField(label='CPF' , max_length = 14 , help_text='Atenção: SOMENTE OS NÚMEROS' , required = True )
    rg = forms.CharField(label='RG' , max_length = 14 , help_text='Atenção: SOMENTE OS NÚMEROS', required = True)
    password = forms.CharField(label= "Senha", widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nome','tipo','email','cpf','rg','password','lattes','area_conhecimento_cnpq','curso_graduacao_vinculado','instituicao']
        
        
class BuscaAlunoForm(forms.Form):
    nome = forms.CharField(label='Nome pesquisador ou parte dele', required=False)
    curso = forms.CharField(label='Nome curso ou parte dele', required=False)