# Generated by Django 2.2.13 on 2020-07-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0008_auto_20200311_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='area_conhecimento_cnpq',
            field=models.CharField(choices=[('CIÊNCIAS DA SAÚDE', 'Ciências da Saúde'), ('CIÊNCIAS HUMANAS', 'Ciências Humanas'), ('CIÊNCIAS SOCIAIS', 'Ciências Sociais'), ('CIÊNCIAS TECNOLÓGICAS', 'Ciências Tecnológicas')], max_length=50, verbose_name='Área de conhecimento *'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(help_text='Atenção: SOMENTE OS NÚMEROS', max_length=14, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='curso_pos_graduacao',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Curso de pós-graduação vinculado'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='lattes',
            field=models.CharField(help_text="Clique <a href='http://buscatextual.cnpq.br/buscatextual' target='_blank'> aqui </a> para descobrir", max_length=100, verbose_name='Lattes *'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rg',
            field=models.CharField(help_text='Atenção: SOMENTE OS NÚMEROS', max_length=14, verbose_name='RG'),
        ),
    ]
