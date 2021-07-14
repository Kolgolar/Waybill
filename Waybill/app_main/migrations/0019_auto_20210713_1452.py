# Generated by Django 3.2.5 on 2021-07-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0018_rename_stops_stop'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stop',
            options={'verbose_name': 'Остановка', 'verbose_name_plural': 'Остановки'},
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=5, verbose_name='Номер')),
                ('stops', models.ManyToManyField(to='app_main.Stop')),
            ],
            options={
                'verbose_name': 'Маршрут',
                'verbose_name_plural': 'Маршруты',
            },
        ),
    ]
