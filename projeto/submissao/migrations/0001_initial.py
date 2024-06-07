# Generated by Django 2.2.6 on 2019-10-08 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('edital', '0001_initial'),
        ('instituicao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submissao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_execucao', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome da instituição de execução do projeto')),
                ('area', models.CharField(choices=[('CIÊNCIAS DA SAÚDE', 'Ciências da Saúde'), ('CIÊNCIAS HUMANAS', 'Ciências Humanas'), ('CIÊNCIAS SOCIAIS', 'Ciências Sociais'), ('CIÊNCIAS TECNOLÓGICAS', 'Ciências Tecnológicas')], max_length=25, verbose_name='Área de ensino, pesquisa e extensão de execução do projeto *')),
                ('curso_graduacao_vinculado', models.CharField(help_text='Nome do curso que está lotado', max_length=50, verbose_name='Curso de graduação vinculado *')),
                ('curso_pos_graduacao', models.CharField(blank=True, help_text='Caso esteja vinculado', max_length=50, null=True, verbose_name='Curso de pós-graduação em que orienta')),
                ('grupo_pesquisa', models.CharField(blank=True, help_text='Caso esteja vinculado', max_length=50, null=True, verbose_name='Grupo de pesquisa vinculado')),
                ('titulo', models.TextField(max_length=200, verbose_name='Título do projeto (200 caracteres) *')),
                ('resumo', models.TextField(max_length=2000, verbose_name='Resumo do projeto (2000 caracteres) *')),
                ('palavras_chave', models.TextField(max_length=100, verbose_name='Palavras-chave: 3 a 5 expressões separadas por ponto-e-vírgula *')),
                ('arquivo_projeto', models.FileField(blank=True, help_text='Use arquivo .pdf para enviar seu projeto', null=True, upload_to='midias', verbose_name='Arquivo anexo do projeto *')),
                ('colaborador', models.ManyToManyField(blank=True, help_text='Para selecionar ou deselecionar um colaborador pressione CTRL + Botão Esquerdo do mouse ou Command + Botão Esquerdo do mouse', null=True, related_name='colaborador', to=settings.AUTH_USER_MODEL)),
                ('edital', models.ForeignKey(help_text='Campo obrigatório como todos os que tiverem *', on_delete=django.db.models.deletion.PROTECT, to='edital.Edital')),
                ('instituicoes_parceiras', models.ManyToManyField(blank=True, help_text='Para selecionar ou deselecionar uma instituição parceira pressione CTRL + Botão Esquerdo do mouse ou Command + Botão Esquerdo do mouse', null=True, to='instituicao.Instituicao')),
                ('responsavel', models.ForeignKey(help_text='Campo obrigatório como todos os que tiverem *', on_delete=django.db.models.deletion.PROTECT, related_name='responsavel', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['titulo', 'responsavel'],
            },
        ),
    ]
