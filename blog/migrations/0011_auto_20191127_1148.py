# Generated by Django 2.1 on 2019-11-26 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20191127_1146'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menuitem',
            options={'ordering': ['lft']},
        ),
    ]
