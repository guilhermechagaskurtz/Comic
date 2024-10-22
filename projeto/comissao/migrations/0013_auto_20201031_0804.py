# Generated by Django 2.2.13 on 2020-10-31 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comissao', '0012_auto_20200915_1555'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comissao',
            options={'ordering': ['-status', 'dt_avaliacao_comissao', 'avaliacao_comissao']},
        ),
        migrations.AlterField(
            model_name='comissao',
            name='status',
            field=models.CharField(choices=[('APROVADO', 'Aprovado'), ('EM ANÁLISE', 'Em Análise'), ('EM EDIÇÃO', 'Em Edição'), ('EM PÓS CORREÇÃO', 'Em Pós Correção'), ('PENDENTE', 'Pendente'), ('REPROVADO', 'Reprovado'), ('TRANCADO', 'Trancado')], default='EM ANÁLISE', max_length=25, verbose_name='Status final do projeto *'),
        ),
    ]
