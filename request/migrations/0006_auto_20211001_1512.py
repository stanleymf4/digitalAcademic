# Generated by Django 3.2.7 on 2021-10-01 20:12

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0005_auto_20211001_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='letter_text',
            field=ckeditor.fields.RichTextField(verbose_name='contenido'),
        ),
        migrations.CreateModel(
            name='LetterService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=50, verbose_name='modificado por')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='fecha de modicación')),
                ('letter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.letter', verbose_name='carta')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.service', verbose_name='servicio')),
            ],
            options={
                'verbose_name': 'carta asociada a servicio',
                'verbose_name_plural': 'cartas asociadas a servicios',
            },
        ),
    ]