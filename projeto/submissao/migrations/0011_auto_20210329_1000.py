# Generated by Django 2.2.13 on 2021-03-29 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissao', '0010_auto_20201031_0718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submissao',
            name='arquivo_anexo',
        ),
        migrations.RemoveField(
            model_name='submissao',
            name='arquivo_parecer_substanciado',
        ),
        migrations.AddField(
            model_name='submissao',
            name='arquivo_relatorio_final',
            field=models.FileField(blank=True, help_text='Quando carregar o anexo, faça registro no campo de Registros e Observações', null=True, upload_to='midias', verbose_name='Arquivo relatório final e devolutiva do projeto'),
        ),
        migrations.AddField(
            model_name='submissao',
            name='arquivo_relatorio_parcial',
            field=models.FileField(blank=True, help_text='Use arquivo .pdf para enviar o parecer substanciado', null=True, upload_to='midias', verbose_name='Arquivo do relatório parcial das atividades do projeto'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='arquivo_comite_etica',
            field=models.FileField(blank=True, help_text='Use arquivo .pdf para enviar a carta do Comitê de Ética', null=True, upload_to='midias', verbose_name='Arquivo do parecer consubstanciado do CEP'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='registros_apos_aprovacao',
            field=models.TextField(blank=True, help_text='Use sempre este espaço se precisar registrar alguma alteração ou ponderar sobre algo', max_length=5000, null=True, verbose_name='Registros e observações no projeto após aprovação'),
        ),
    ]
