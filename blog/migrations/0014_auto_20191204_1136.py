# Generated by Django 2.1 on 2019-12-03 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20191204_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категорию', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_pub'], 'verbose_name': 'новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='wateroff',
            options={'ordering': ['-id'], 'verbose_name': 'отключение ХВС', 'verbose_name_plural': 'Отключения ХВС'},
        ),
    ]
