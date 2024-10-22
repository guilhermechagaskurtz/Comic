# Generated by Django 2.2.13 on 2021-05-22 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_arquivo', models.CharField(help_text='* Campos obrigatórios', max_length=100, unique=True, verbose_name='Descrição do documento *')),
                ('arquivo', models.FileField(help_text='Use arquivo .pdf para o documento', upload_to='midias', verbose_name='Arquivo do documento')),
                ('is_active', models.BooleanField(default=True, help_text='Se ativo, o documento pode ser usado no sistema', verbose_name='Ativo')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, verbose_name='Hash')),
            ],
            options={
                'verbose_name': 'documento',
                'verbose_name_plural': 'documentos',
                'ordering': ['-is_active', 'descricao_arquivo'],
            },
        ),
    ]
