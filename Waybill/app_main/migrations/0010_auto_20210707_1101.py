# Generated by Django 3.2.5 on 2021-07-07 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0009_alter_transport_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waybill',
            name='date',
        ),
        migrations.RemoveField(
            model_name='waybill',
            name='transport',
        ),
    ]
