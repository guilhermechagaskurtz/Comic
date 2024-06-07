# Generated by Django 2.2.6 on 2019-10-08 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('sigla', models.CharField(max_length=20, verbose_name='Sigla')),
                ('site', models.CharField(max_length=100, verbose_name='Site instituição')),
                ('contato', models.CharField(blank=True, max_length=100, verbose_name='Nome completo do contato')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='Email do contato')),
                ('telefone', models.CharField(blank=True, max_length=100, verbose_name='Telefone do contato')),
            ],
            options={
                'ordering': ['sigla'],
            },
        ),
    ]
