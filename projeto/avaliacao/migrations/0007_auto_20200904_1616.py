# Generated by Django 2.2.13 on 2020-09-04 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0006_auto_20200711_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='status',
            field=models.CharField(choices=[('APROVADO', 'Aprovado'), ('REPROVADO', 'Reprovado'), ('EM ANÁLISE', 'Em análise'), ('EM EDIÇÃO', 'Em edição'), ('PENDENTE', 'Pendente'), ('PÓS CORREÇÃO', 'Pós correção'), ('TRANCADO', 'Trancado')], default='EM ANÁLISE', max_length=25, verbose_name='Status do projeto'),
        ),
    ]
