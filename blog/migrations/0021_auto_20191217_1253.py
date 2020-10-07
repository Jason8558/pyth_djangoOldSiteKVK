# Generated by Django 2.1 on 2019-12-17 00:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20191217_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_pub',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 12, 53, 51, 709211), verbose_name='дата публикации'),
        ),
        migrations.AlterField(
            model_name='wateroff',
            name='date_of_off',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 12, 53, 51, 722264), verbose_name='дата отключения'),
        ),
        migrations.AlterField(
            model_name='wateroff',
            name='date_of_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 17, 12, 53, 51, 722264), verbose_name='дата подачи'),
        ),
    ]
