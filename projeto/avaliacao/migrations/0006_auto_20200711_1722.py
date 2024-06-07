# Generated by Django 2.2.13 on 2020-07-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacao', '0005_auto_20200523_0053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='avaliacao',
            options={'ordering': ['status', '-dt_limite_avaliacao', 'submissao']},
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_assitencia_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='O projeto interfere na rotina ou prática assistencial vigente de modo significativo?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_assitencia_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='O projeto interfere na rotina ou prática assistencial vigente de modo significativo?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_cronograma_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Há um cronograma de atividades?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_cronograma_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Há um cronograma de atividades?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_introducao_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='A introdução está adequada?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_introducao_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='A introdução está adequada?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_justificativa_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Existe uma justificativa coerente?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_justificativa_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Existe uma justificativa coerente?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_amostra_estudo_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, há definição da amostra para estudos quantitativos?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_amostra_estudo_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, há definição da amostra para estudos quantitativos?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_assentimento_estudo_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, apresenta termo de assentimento em apêndice?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_assentimento_estudo_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, apresenta termo de assentimento em apêndice?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_coleta_estudo_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, o período de coleta de dados está definido?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_coleta_estudo_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, o período de coleta de dados está definido?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_coleta_instrumento_estudo_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, o projeto inclui um instrumento de coleta de dados em apêndice?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_coleta_instrumento_estudo_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, o projeto inclui um instrumento de coleta de dados em apêndice?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_confidencialidade_estudo_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, apresenta termo de confidencialidade?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_confidencialidade_estudo_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, apresenta termo de confidencialidade?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_consentimento_estudo_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, apresenta termo de consentimento livre e esclarecido em apêndice?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_consentimento_estudo_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, apresenta termo de consentimento livre e esclarecido em apêndice?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_desenho_estudo_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, o desenho do estudo está claramente definido?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_desenho_estudo_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, o desenho do estudo está claramente definido?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_etica_estudo_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, os aspectos éticos estão descritos?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_etica_estudo_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, os aspectos éticos estão descritos?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_exequivel_estudo_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, o projeto é exequível na instituição/unidade definido?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_exequivel_estudo_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, o projeto é exequível na instituição/unidade definido?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_inclusao_estudo_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, os critérios de inclusão e/ou exclusão estão claros?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_inclusao_estudo_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, os critérios de inclusão e/ou exclusão estão claros?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_local_estudo_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, o local de realização do estudo e a população estão claramente definidos?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_local_estudo_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, o local de realização do estudo e a população estão claramente definidos?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_riscos_estudo_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, os riscos do estudo estão descritos?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_metodologia_riscos_estudo_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Metodologicamente, os riscos do estudo estão descritos?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_mudanca_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='O projeto prevê mudanças de alguma prática institucional vigente?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_mudanca_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='O projeto prevê mudanças de alguma prática institucional vigente?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_nova_pratica_assistencial_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='O projeto prevê implementação de nova prática assistencial?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_nova_pratica_assistencial_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='O projeto prevê implementação de nova prática assistencial?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_objetivos_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Os objetivos são claros e exequíveis?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_objetivos_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Os objetivos são claros e exequíveis?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_orcamento_agencia_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='O orçamento é de agência de fomento?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_orcamento_agencia_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='O orçamento é de agência de fomento?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_orcamento_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Projeto possui orçamento?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_orcamento_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Projeto possui orçamento?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_produto_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='O projeto prevê desenvolvimento de produto ou tecnologia leve-dura ou dura?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_produto_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='O projeto prevê desenvolvimento de produto ou tecnologia leve-dura ou dura?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_referencias_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Há referências bibliográficas no projeto?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_referencias_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='Há referências bibliográficas no projeto?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_relevancia_responsavel',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='O projeto tem relevância para a instituição envolvida?'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='tem_relevancia_suplente',
            field=models.CharField(blank=True, choices=[('SIM', 'Sim'), ('NÃO', 'Não'), ('EM PARTE', 'Em parte'), ('NÃO SE APLICA', 'Não se aplica')], max_length=25, null=True, verbose_name='O projeto tem relevância para a instituição envolvida?'),
        ),
    ]
