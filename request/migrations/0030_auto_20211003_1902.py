# Generated by Django 3.2.7 on 2021-10-04 00:02

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('request', '0029_auto_20211003_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasourcevalue',
            name='data_related',
            field=models.CharField(max_length=4, null=True, verbose_name='dato de fuente relacionada'),
        ),
        migrations.CreateModel(
            name='ServiceConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('population_filter_api', models.CharField(max_length=2000, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('delivery_days', models.IntegerField(max_length=2, null=True)),
                ('bussiness_days', models.BooleanField(null=True)),
                ('is_active', models.BooleanField(null=True)),
                ('comments', ckeditor.fields.RichTextField(verbose_name='comentarios del servicio')),
                ('user_id', models.CharField(blank=True, max_length=50, verbose_name='modificado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='fecha de modicación')),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.group')),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.service')),
            ],
            options={
                'verbose_name': 'regla del servicio',
                'verbose_name_plural': 'reglas del servicio',
                'db_table': 'request_service_configuration',
            },
        ),
    ]