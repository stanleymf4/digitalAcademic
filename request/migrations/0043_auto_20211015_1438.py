# Generated by Django 3.2.7 on 2021-10-15 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0042_auto_20211015_0859'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='letter',
            options={'verbose_name': 'Marco legal del servicio', 'verbose_name_plural': 'Marco legal de servicios'},
        ),
        migrations.AlterModelOptions(
            name='letterservice',
            options={'verbose_name': 'servicio y marco legal', 'verbose_name_plural': 'servicios y marco legal'},
        ),
        migrations.AlterField(
            model_name='componentsubsection',
            name='component_action',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='request.componentsubsection', verbose_name='componente de acción'),
        ),
        migrations.AlterField(
            model_name='componentsubsection',
            name='value_component_action',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='valor componente acción'),
        ),
        migrations.AlterField(
            model_name='letter',
            name='description',
            field=models.CharField(max_length=100, unique=True, verbose_name='descripción'),
        ),
        migrations.AlterField(
            model_name='letterservice',
            name='description',
            field=models.CharField(default=False, max_length=100, verbose_name='descripción'),
        ),
        migrations.AlterField(
            model_name='letterservice',
            name='letter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='request.letter', verbose_name='marco legal'),
        ),
        migrations.AlterField(
            model_name='letterservice',
            name='order_display',
            field=models.IntegerField(verbose_name='orden para mostrar'),
        ),
        migrations.AlterField(
            model_name='letterservice',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='request.service', verbose_name='servicio'),
        ),
        migrations.AlterUniqueTogether(
            name='letterservice',
            unique_together={('service', 'letter')},
        ),
    ]
