# Generated by Django 3.2.7 on 2021-10-04 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0039_auto_20211003_2343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='componentsubsection',
            options={'verbose_name': 'subsección y componente', 'verbose_name_plural': 'subsecciones y componentes'},
        ),
        migrations.AddField(
            model_name='componentsubsection',
            name='order_display',
            field=models.IntegerField(null=True, verbose_name='orden despliegue'),
        ),
    ]
