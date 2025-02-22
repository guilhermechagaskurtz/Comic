# Generated by Django 2.2.13 on 2021-03-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissao', '0011_auto_20210329_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissao',
            name='arquivo_emenda1',
            field=models.FileField(blank=True, help_text='Use arquivo .pdf para enviar a emenda', null=True, upload_to='midias', verbose_name='Arquivo para PRIMEIRA emenda'),
        ),
        migrations.AddField(
            model_name='submissao',
            name='arquivo_emenda2',
            field=models.FileField(blank=True, help_text='Use arquivo .pdf para enviar a emenda', null=True, upload_to='midias', verbose_name='Arquivo para SEGUNDA emenda'),
        ),
        migrations.AddField(
            model_name='submissao',
            name='arquivo_emenda3',
            field=models.FileField(blank=True, help_text='Use arquivo .pdf para enviar a emenda', null=True, upload_to='midias', verbose_name='Arquivo para TERCEIRA emenda'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='arquivo_relatorio_final',
            field=models.FileField(blank=True, help_text='Use arquivo .pdf para enviar o relatório final', null=True, upload_to='midias', verbose_name='Arquivo relatório final e devolutiva do projeto'),
        ),
        migrations.AlterField(
            model_name='submissao',
            name='arquivo_relatorio_parcial',
            field=models.FileField(blank=True, help_text='Use arquivo .pdf para enviar o relatório parcial', null=True, upload_to='midias', verbose_name='Arquivo do relatório parcial das atividades do projeto. DEVE ser atualizado com frequência'),
        ),
    ]
