# Generated by Django 2.1 on 2019-12-05 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20191204_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(db_index=True, max_length=150, verbose_name='заголовок'),
        ),
    ]
