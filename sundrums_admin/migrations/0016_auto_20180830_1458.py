# Generated by Django 2.1 on 2018-08-30 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sundrums_admin', '0015_auto_20180830_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipe_kurs',
            name='name',
            field=models.CharField(blank=True, default=' ', max_length=64, null=True, verbose_name='пароль для открытия статии '),
        ),
    ]
