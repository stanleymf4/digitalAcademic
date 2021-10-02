# Generated by Django 3.2.7 on 2021-10-01 19:37

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0004_auto_20211001_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='descripción')),
                ('letter_text', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('user_id', models.CharField(blank=True, max_length=50, verbose_name='modificado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='fecha de modicación')),
            ],
            options={
                'verbose_name': 'Carta',
                'verbose_name_plural': 'Cartas',
            },
        ),
        migrations.AlterField(
            model_name='service',
            name='category_service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.categoryservice', verbose_name='categoria de servicio'),
        ),
    ]
