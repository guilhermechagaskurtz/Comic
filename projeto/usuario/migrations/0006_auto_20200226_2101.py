# Generated by Django 2.2.6 on 2020-02-27 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_auto_20191120_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Se ativo o usuário tem permissão para acessar o sistema', verbose_name='Ativo'),
        ),
    ]
