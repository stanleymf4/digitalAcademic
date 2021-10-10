# Generated by Django 3.2.7 on 2021-10-03 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0023_alter_entity_root_entity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='category_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='request.categoryservice', verbose_name='categoria de servicio'),
        ),
        migrations.AlterField(
            model_name='service',
            name='entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='request.entity', verbose_name='entidad prestadora'),
        ),
    ]