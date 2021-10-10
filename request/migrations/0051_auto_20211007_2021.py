# Generated by Django 3.2.7 on 2021-10-08 01:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0050_auto_20211007_2008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='priority',
            options={'verbose_name': 'prioridad de servicio', 'verbose_name_plural': 'prioridades de servicios'},
        ),
        migrations.AddField(
            model_name='priority',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 10, 8, 1, 21, 40, 678077, tzinfo=utc), verbose_name='fecha de creación'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='priority',
            name='modified_at',
            field=models.DateTimeField(auto_now=True, verbose_name='fecha de modicación'),
        ),
        migrations.AddField(
            model_name='priority',
            name='user_id',
            field=models.CharField(blank=True, max_length=50, verbose_name='modificado por'),
        ),
        migrations.AlterModelTable(
            name='priority',
            table='request_priority',
        ),
    ]
