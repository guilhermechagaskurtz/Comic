# Generated by Django 3.1.5 on 2021-05-23 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comissao', '0013_auto_20201031_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comissao',
            name='status',
            field=models.CharField(choices=[('APROVADO', 'Aprovado'), ('EM ANÁLISE', 'Em Análise'), ('EM EDIÇÃO', 'Em Edição'), ('PÓS CORREÇÃO', 'Pós Correção'), ('PENDENTE', 'Pendente'), ('REPROVADO', 'Reprovado'), ('TRANCADO', 'Trancado'), ('RETIRADO PELO PROFESSOR', 'Retirado pelo professor'), ('RETIRADO PELO COMIC', 'Retirado pelo COMIC')], default='EM ANÁLISE', max_length=25, verbose_name='Status final do projeto *'),
        ),
    ]
