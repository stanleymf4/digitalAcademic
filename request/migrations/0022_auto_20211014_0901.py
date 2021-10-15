# Generated by Django 3.2.7 on 2021-10-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0021_alter_serviceconfiguration_is_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceconfiguration',
            name='bussiness_days',
            field=models.BooleanField(default=False, verbose_name='dias laborales'),
        ),
        migrations.AlterField(
            model_name='serviceconfiguration',
            name='delivery_days',
            field=models.IntegerField(default=False, verbose_name='dias de entrega'),
        ),
        migrations.AlterField(
            model_name='serviceconfiguration',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='activo'),
        ),
        migrations.AlterField(
            model_name='serviceconfiguration',
            name='is_form_active',
            field=models.BooleanField(default=False, verbose_name='formulario activo'),
        ),
        migrations.AlterField(
            model_name='serviceconfiguration',
            name='is_payment',
            field=models.BooleanField(default=False, verbose_name='requiere pago'),
        ),
        migrations.AlterField(
            model_name='serviceconfiguration',
            name='working_hours',
            field=models.BooleanField(default=False, verbose_name='horas laborales'),
        ),
    ]
