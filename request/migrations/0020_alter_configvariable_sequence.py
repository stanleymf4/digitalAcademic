# Generated by Django 3.2.7 on 2021-10-02 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0019_configvariable_sequence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configvariable',
            name='sequence',
            field=models.IntegerField(default=1, verbose_name='secuencia'),
        ),
    ]
