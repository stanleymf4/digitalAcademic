# Generated by Django 3.2.7 on 2021-10-15 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0037_alter_subsectionserviceform_section_main_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainformsection',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='activo'),
        ),
        migrations.AlterField(
            model_name='subsectionserviceform',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='activo'),
        ),
    ]