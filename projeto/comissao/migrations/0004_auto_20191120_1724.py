# Generated by Django 2.2.6 on 2019-11-20 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comissao', '0003_remove_comissao_parecer_comissao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comissao',
            name='arquivo_resposta_comissao',
            field=models.FileField(help_text='Use arquivo .pdf para a resposta', upload_to='midias', verbose_name='Arquivo padrão de resposta a submissão do projeto *'),
        ),
        migrations.AlterField(
            model_name='comissao',
            name='avaliacao_comissao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='avaliacao.Avaliacao', verbose_name='Selecione uma avaliação de projeto submetido para parecer da comissão *'),
        ),
        migrations.AlterField(
            model_name='comissao',
            name='status',
            field=models.CharField(choices=[('APROVADO', 'Aprovado'), ('PENDENTE', 'Pendente'), ('REPROVADO', 'Reprovado')], max_length=25, verbose_name='Status final do projeto *'),
        ),
    ]