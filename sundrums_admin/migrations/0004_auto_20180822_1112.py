# Generated by Django 2.1 on 2018-08-22 08:12

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('sundrums_admin', '0003_topic_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, help_text='загрузите сюда изображение для категории это будет в плитках навигации', upload_to='static/media/categories_images/', verbose_name=' главное изображение для отдельных статей'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='description',
            field=tinymce.models.HTMLField(blank=True, default=' ', null=True, verbose_name=' все описание статьи можно вставлять код html целиком'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='name',
            field=models.CharField(blank=True, default=' ', max_length=255, null=True, verbose_name='имя статьи кратко это будет в меню навигации'),
        ),
    ]
