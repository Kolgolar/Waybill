# Generated by Django 3.2.5 on 2021-07-14 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0021_auto_20210714_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='inlinestop',
            name='time',
            field=models.TimeField(null=True, verbose_name='Время'),
        ),
        migrations.AddField(
            model_name='route',
            name='route_type',
            field=models.CharField(choices=[('Завоз', 'Завоз'), ('Вывоз', 'Вывоз')], default='Завоз', max_length=5, verbose_name='Тип поездки'),
        ),
        migrations.AlterField(
            model_name='inlinestop',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_main.stop'),
        ),
        migrations.AlterField(
            model_name='inlinestop',
            name='route',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_main.route'),
        ),
        migrations.AlterField(
            model_name='route',
            name='description',
            field=models.TextField(max_length=300, null=True, verbose_name='Описание'),
        ),
    ]
