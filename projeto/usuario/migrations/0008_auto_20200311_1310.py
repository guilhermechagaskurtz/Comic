# Generated by Django 2.2.6 on 2020-03-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0007_usuario_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='lattes',
            field=models.CharField(blank=True, help_text='Acesse http://lattes.cnpq.br para descobrir', max_length=100, null=True, verbose_name='Lattes *'),
        ),
    ]
