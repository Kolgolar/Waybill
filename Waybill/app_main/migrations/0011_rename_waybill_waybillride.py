# Generated by Django 3.2.5 on 2021-07-07 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0010_auto_20210707_1101'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WayBill',
            new_name='WayBillRide',
        ),
    ]