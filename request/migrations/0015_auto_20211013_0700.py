# Generated by Django 3.2.7 on 2021-10-13 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0014_auto_20211013_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actionablecomponent',
            name='rule_subsection',
        ),
        migrations.AddField(
            model_name='actionablecomponent',
            name='accion_visible',
            field=models.BooleanField(default=False, null=True, verbose_name='accion: visible'),
        ),
        migrations.AddField(
            model_name='actionablecomponent',
            name='rule_component_action',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.PROTECT, to='request.componentactiondetail', verbose_name='subsección de servicio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='actionablecomponent',
            name='component_action_emisor',
            field=models.IntegerField(blank=True, choices=[(1, 'Cedula de ciudadania'), (2, 'Ciudad de Residencia'), (3, 'XXXX'), (4, 'SSSSS'), (5, 'Cedula de ciudadanía'), (6, 'Programa académico'), (7, 'Periodo académico'), (8, 'Programas Académios'), (9, 'Prueba Componente')], verbose_name='componente emisor'),
        ),
        migrations.AlterField(
            model_name='actionablecomponent',
            name='component_action_receptor',
            field=models.IntegerField(blank=True, choices=[(1, 'Cedula de ciudadania'), (2, 'Ciudad de Residencia'), (3, 'XXXX'), (4, 'SSSSS'), (5, 'Cedula de ciudadanía'), (6, 'Programa académico'), (7, 'Periodo académico'), (8, 'Programas Académios'), (9, 'Prueba Componente')], verbose_name='componente receptor'),
        ),
    ]
