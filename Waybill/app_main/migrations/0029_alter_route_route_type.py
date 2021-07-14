# Generated by Django 3.2.5 on 2021-07-14 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0028_alter_route_route_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='route_type',
            field=models.CharField(choices=[('Вывоз', 'Вывоз'), ('Завоз', 'Завоз')], default='Завоз', max_length=5, verbose_name='Тип поездки'),
        ),
    ]
