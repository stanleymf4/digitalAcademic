# Generated by Django 3.2.7 on 2021-10-04 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0040_auto_20211003_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentsubsection',
            name='key_head',
            field=models.CharField(choices=[], max_length=80, null=True, verbose_name='key head'),
        ),
    ]
