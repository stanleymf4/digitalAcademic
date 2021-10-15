# Generated by Django 3.2.7 on 2021-10-13 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0013_auto_20211013_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actionablecomponent',
            name='component_action_emisor',
            field=models.IntegerField(blank=True, choices=[(1, 'Cedula de ciudadania'), (2, 'Ciudad de Residencia'), (3, 'XXXX'), (4, 'SSSSS'), (5, 'Cedula de ciudadanía')], verbose_name='componente emisor'),
        ),
        migrations.AlterField(
            model_name='actionablecomponent',
            name='component_action_receptor',
            field=models.IntegerField(blank=True, choices=[(1, 'Cedula de ciudadania'), (2, 'Ciudad de Residencia'), (3, 'XXXX'), (4, 'SSSSS'), (5, 'Cedula de ciudadanía')], verbose_name='componente receptor'),
        ),
        migrations.AlterField(
            model_name='actionablecomponent',
            name='rule_subsection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='request.subsectionserviceform', verbose_name='subsección de servicio'),
        ),
        migrations.AlterUniqueTogether(
            name='actionablecomponent',
            unique_together={('component_action_emisor', 'component_action_receptor', 'value_component_emisor')},
        ),
    ]