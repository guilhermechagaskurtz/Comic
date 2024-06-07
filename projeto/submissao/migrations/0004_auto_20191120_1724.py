# Generated by Django 2.2.6 on 2019-11-20 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submissao', '0003_auto_20191119_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submissao',
            name='arquivo_projeto',
            field=models.FileField(help_text='Use arquivo .pdf para enviar seu projeto', upload_to='midias', verbose_name='Arquivo anexo do projeto *'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='arquivo_resposta_comissao',
            field=models.FileField(blank=True, help_text='Use arquivo .pdf', null=True, upload_to='midias', verbose_name='Arquivo do parecer da comissão *'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='colaborador',
            field=models.ManyToManyField(blank=True, help_text='Para selecionar ou deselecionar um colaborador pressione CTRL + Botão Esquerdo do mouse ou Command + Botão Esquerdo do mouse', null=True, related_name='colaborador', to=settings.AUTH_USER_MODEL, verbose_name='Colaborador(es)'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='curso_pos_graduacao',
            field=models.CharField(blank=True, help_text='Nome dos cursos associados ao projeto separados por ponto-e-vírgula', max_length=100, null=True, verbose_name='Curso(s) de pós-graduação vinculado(s)'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='edital',
            field=models.ForeignKey(help_text='Campo obrigatório como todos os que tiverem *', on_delete=django.db.models.deletion.PROTECT, to='edital.Edital', verbose_name='Edital vigente *'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='instituicoes_parceiras',
            field=models.ManyToManyField(blank=True, help_text='Para selecionar ou deselecionar uma instituição parceira pressione CTRL + Botão Esquerdo do mouse ou Command + Botão Esquerdo do mouse', null=True, to='instituicao.Instituicao', verbose_name='Instituições parceiras'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='local_execucao',
            field=models.CharField(help_text='Campo obrigatório como todos os que tiverem *', max_length=150, verbose_name='Nome da instituição de execução do projeto *'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='responsavel',
            field=models.ForeignKey(help_text='Você deve selecionar o professor responsável', on_delete=django.db.models.deletion.PROTECT, related_name='responsavel', to=settings.AUTH_USER_MODEL, verbose_name='Responsável pelo projeto *'),
        ),
    ]
