# Generated by Django 2.1 on 2018-08-21 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sundrums_admin', '0002_auto_20180821_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='is_active',
            field=models.BooleanField(default='True', verbose_name='вкл? '),
        ),
    ]
