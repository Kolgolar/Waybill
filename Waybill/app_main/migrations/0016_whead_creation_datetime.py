# Generated by Django 3.2.5 on 2021-07-08 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0015_rename_ride_id_wride_head_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='whead',
            name='creation_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]
