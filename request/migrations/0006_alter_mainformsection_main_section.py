# Generated by Django 3.2.7 on 2021-10-11 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0005_auto_20211011_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainformsection',
            name='main_section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='main_section_form', to='request.mainsection', unique=True, verbose_name='Sección principal formulario'),
        ),
    ]
