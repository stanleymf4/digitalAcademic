# Generated by Django 3.2.7 on 2021-10-08 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0056_auto_20211008_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceconfiguration',
            name='days_validity_document',
            field=models.IntegerField(default=0, verbose_name='dias de vigencia documento'),
        ),
    ]
