# Generated by Django 2.1 on 2019-12-17 01:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20191217_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_pub',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 13, 7, 38, 271570), verbose_name='дата публикации'),
        ),
        migrations.AlterField(
            model_name='wateroff',
            name='date_of_off',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 13, 7, 38, 285695), verbose_name='дата отключения'),
        ),
        migrations.AlterField(
            model_name='wateroff',
            name='date_of_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 13, 7, 38, 285695), verbose_name='дата подачи'),
        ),
    ]
