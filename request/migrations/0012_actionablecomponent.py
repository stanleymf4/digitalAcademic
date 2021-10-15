# Generated by Django 3.2.7 on 2021-10-13 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0011_remove_componentsubsection_actionable_component'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionableComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_component_emisor', models.CharField(max_length=10, verbose_name='valor componente emisor')),
                ('component_action_emisor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='request.componentsubsection', verbose_name='Componente receptor')),
                ('rule_subsection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='request.subsectionserviceform', verbose_name='Subsección de servicio')),
            ],
            options={
                'verbose_name': 'componente de acción',
                'verbose_name_plural': 'componentes de acción',
                'db_table': 'request_component_actionable',
            },
        ),
    ]
