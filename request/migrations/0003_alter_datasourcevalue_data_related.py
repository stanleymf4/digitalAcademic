# Generated by Django 3.2.7 on 2021-10-11 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_auto_20211011_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasourcevalue',
            name='data_related',
            field=models.CharField(blank=True, max_length=4, null=True, verbose_name='dato de fuente relacionada'),
        ),
    ]