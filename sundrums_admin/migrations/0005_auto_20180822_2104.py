# Generated by Django 2.1 on 2018-08-22 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sundrums_admin', '0004_auto_20180822_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='button_text',
            field=models.CharField(blank=True, default=' ', max_length=64, null=True, verbose_name='текст кнопки'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, help_text='загрузите сюда изображение для категории это будет в плитках навигации', upload_to='static/media/post_images/', verbose_name=' главное изображение для отдельных статей'),
        ),
    ]
