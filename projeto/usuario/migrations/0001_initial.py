# Generated by Django 2.2.6 on 2019-10-08 22:11

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import usuario.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instituicao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('tipo', models.CharField(choices=[('ADMINISTRADOR', 'Administrador'), ('PROFESSOR', 'Professor'), ('BOLSISTA', 'Bolsista')], default='PROFESSOR', max_length=15, verbose_name='Tipo do usuário')),
                ('nome', models.CharField(help_text='Campo obrigatório como todos os que tiverem *', max_length=100, verbose_name='Nome *')),
                ('email', models.EmailField(db_index=True, max_length=100, unique=True, verbose_name='Email *')),
                ('data_nasc', models.DateField(blank=True, help_text='dd/mm/aaaa', null=True, verbose_name='Data de Nascimento')),
                ('cpf', models.CharField(blank=True, max_length=14, null=True, verbose_name='CPF')),
                ('rg', models.IntegerField(blank=True, null=True, verbose_name='RG')),
                ('matricula', models.CharField(blank=True, max_length=10, null=True, verbose_name='Matricula')),
                ('lattes', models.CharField(blank=True, max_length=100, null=True, verbose_name='Lattes *')),
                ('area_conhecimento_cnpq', models.CharField(blank=True, max_length=50, null=True, verbose_name='Área de conhecimento no CNPq')),
                ('curso_graduacao_vinculado', models.CharField(help_text='Nome do curso que está lotado', max_length=50, verbose_name='Curso de graduação vinculado *')),
                ('curso_pos_graduacao', models.CharField(blank=True, max_length=50, null=True, verbose_name='Curso de pós-graduação em que orienta')),
                ('grupo_pesquisa', models.CharField(blank=True, max_length=50, null=True, verbose_name='Grupo de pesquisa vinculado')),
                ('is_active', models.BooleanField(default=False, help_text='Se ativo o usuário tem permissão para acessar o sistema', verbose_name='Ativo')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='instituicao.Instituicao')),
            ],
            options={
                'verbose_name': 'usuário',
                'verbose_name_plural': 'usuários',
                'ordering': ['nome'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
                ('administradores', usuario.models.AdministradorAtivoManager()),
                ('professores', usuario.models.ProfessorAtivoManager()),
                ('bolsistas', usuario.models.BolsistaAtivoManager()),
            ],
        ),
    ]