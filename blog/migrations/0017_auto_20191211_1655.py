# Generated by Django 2.1 on 2019-12-11 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20191205_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wateroff',
            name='reason',
            field=models.CharField(choices=[('Авария', 'Авария')], max_length=50, verbose_name='причина отключения'),
        ),
    ]