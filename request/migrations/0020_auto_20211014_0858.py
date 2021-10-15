# Generated by Django 3.2.7 on 2021-10-14 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0019_auto_20211014_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceconfiguration',
            name='is_autenticado',
            field=models.BooleanField(default=False, verbose_name='requiere autenticación'),
        ),
        migrations.AddField(
            model_name='serviceconfiguration',
            name='url_form',
            field=models.URLField(max_length=500, null=True, verbose_name='url formulario'),
        ),
        migrations.AddField(
            model_name='serviceconfiguration',
            name='valid_user',
            field=models.BooleanField(default=False, verbose_name='validacion de usuario'),
        ),
    ]
