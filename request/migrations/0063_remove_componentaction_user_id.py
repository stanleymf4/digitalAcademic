# Generated by Django 3.2.7 on 2021-10-10 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0062_alter_componentaction_service_component_section_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='componentaction',
            name='user_id',
        ),
    ]
