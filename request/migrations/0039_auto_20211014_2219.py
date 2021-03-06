# Generated by Django 3.2.7 on 2021-10-15 03:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0038_auto_20211014_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainformsection',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='mainformsection',
            name='modified_at',
        ),
        migrations.RemoveField(
            model_name='mainformsection',
            name='user_id',
        ),
        migrations.AddField(
            model_name='componentsubsection',
            name='component_action',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='request.componentsubsection', verbose_name='componente de acción'),
        ),
        migrations.AddField(
            model_name='componentsubsection',
            name='value_component_action',
            field=models.CharField(max_length=60, null=True, verbose_name='valor componente acción'),
        ),
    ]
