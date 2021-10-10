# Generated by Django 3.2.7 on 2021-10-08 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('request', '0053_auto_20211008_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceconfigurationstatus',
            name='assign_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='usuario asignado'),
        ),
    ]
