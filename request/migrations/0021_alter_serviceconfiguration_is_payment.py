# Generated by Django 3.2.7 on 2021-10-14 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0020_auto_20211014_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceconfiguration',
            name='is_payment',
            field=models.BooleanField(default=False, verbose_name='Requiere pago'),
        ),
    ]
