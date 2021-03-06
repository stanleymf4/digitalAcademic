# Generated by Django 3.2.7 on 2021-10-16 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0048_auto_20211015_2154'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datasourcevalue',
            options={'verbose_name': 'valor de fuente de dato', 'verbose_name_plural': 'valores de fuentes de datos'},
        ),
        migrations.AlterModelOptions(
            name='serviceconfiguration',
            options={'verbose_name': 'regla de servicio', 'verbose_name_plural': 'reglas de servicios'},
        ),
        migrations.AlterField(
            model_name='datasource',
            name='source',
            field=models.CharField(max_length=150, unique=True, verbose_name='Fuente de datos'),
        ),
        migrations.AlterField(
            model_name='datasourcevalue',
            name='code_data',
            field=models.CharField(max_length=4, unique=True, verbose_name='código de lista de opciones'),
        ),
        migrations.AlterField(
            model_name='datasourcevalue',
            name='data_related',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='request.datasourcevalue', to_field='code_data', verbose_name='dato de fuente relacionada'),
        ),
        migrations.AlterField(
            model_name='datasourcevalue',
            name='source_data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='dataSourceValue', to='request.datasource', verbose_name='fuente de datos'),
        ),
        migrations.AlterField(
            model_name='datasourcevalue',
            name='value_data',
            field=models.CharField(max_length=100, verbose_name='descripción de lista de opciones'),
        ),
        migrations.AlterField(
            model_name='mainformsection',
            name='order_display',
            field=models.IntegerField(verbose_name='orden para mostrar'),
        ),
        migrations.AlterField(
            model_name='serviceconfiguration',
            name='comments',
            field=models.TextField(blank=True, null=True, verbose_name='comentarios del servicio'),
        ),
        migrations.AlterField(
            model_name='serviceconfiguration',
            name='delivery_days',
            field=models.IntegerField(verbose_name='días de entrega'),
        ),
        migrations.AlterField(
            model_name='serviceconfiguration',
            name='is_form_active',
            field=models.BooleanField(default=False, verbose_name='formulario disponible'),
        ),
        migrations.AlterField(
            model_name='serviceconfiguration',
            name='url_form',
            field=models.URLField(blank=True, max_length=500, null=True, verbose_name='url formulario'),
        ),
        migrations.AlterField(
            model_name='serviceconfiguration',
            name='valid_user',
            field=models.BooleanField(default=False, verbose_name='validación de usuario'),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='key_config',
            field=models.ForeignKey(blank=True, limit_choices_to={'group_variable': 'SECDF'}, null=True, on_delete=django.db.models.deletion.PROTECT, to='request.configvariable', verbose_name='key config'),
        ),
        migrations.AlterUniqueTogether(
            name='datasourcevalue',
            unique_together={('code_data', 'value_data', 'source_data')},
        ),
    ]
