# Generated by Django 3.2.5 on 2021-07-07 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0013_auto_20210707_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='wride',
            name='ride_id',
            field=models.PositiveIntegerField(default=0, verbose_name='№'),
            preserve_default=False,
        ),
    ]
