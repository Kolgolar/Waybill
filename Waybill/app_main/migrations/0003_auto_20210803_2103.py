# Generated by Django 3.2.6 on 2021-08-03 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0002_auto_20210719_1544'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inlinestop',
            options={'verbose_name': 'Остановки', 'verbose_name_plural': 'Остановки'},
        ),
        migrations.AlterField(
            model_name='route',
            name='route_type',
            field=models.CharField(choices=[('Вывоз', 'Вывоз'), ('Завоз', 'Завоз')], default='Завоз', max_length=5, verbose_name='Тип поездки'),
        ),
    ]
