# Generated by Django 3.2.7 on 2021-10-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0059_auto_20211010_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='componentaction',
            name='service_component_group_id',
            field=models.CharField(choices=[], max_length=10, null=True, verbose_name='grupo de componentes'),
        ),
        migrations.AlterField(
            model_name='componentaction',
            name='service_component_section_id',
            field=models.CharField(choices=[], max_length=10, null=True, verbose_name='secciones de componentes'),
        ),
    ]
