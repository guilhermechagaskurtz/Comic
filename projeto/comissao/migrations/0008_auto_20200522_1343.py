# Generated by Django 2.2.6 on 2020-05-22 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comissao', '0007_auto_20200522_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comissao',
            old_name='arquivo1_resposta_comissao',
            new_name='arquivo_parecer_comissao',
        ),
        migrations.RenameField(
            model_name='comissao',
            old_name='arquivo2_resposta_comissao',
            new_name='arquivo_parecer_comissao_pendencia',
        ),
    ]
