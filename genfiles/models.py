from tinymce.models import HTMLField 
from django.db import models 
""" begin slider"""
class slider(models.Model):
      name =  models.CharField(  max_length = 64, blank=True,  null=True, default='', verbose_name= ' имя слайда')
      image =  models.ImageField(  max_length = 64, blank=True, upload_to='sliders_images/', help_text = 'изображения для слайда',  default='', verbose_name= 'путь к картинке')
      description =  models.CharField(  max_length = 250, blank=True,  null=True, default='', verbose_name= ' описание или содержание слайда')
      link =  models.CharField(  max_length = 64, blank=True,  null=True, default='#featured-services', verbose_name= 'ссылка если нужна')
      is_active =  models.BooleanField(     null=True, default=True, verbose_name='добавить для вывода на основной странице?')
      active_slide =  models.CharField(  max_length = 16, blank=True,  null=True, default='', verbose_name= 'активный ли это слайд (внимание написать active только для первого слайда в остальных случаях пустое значение) ')
      text_button =  models.CharField(  max_length = 64, blank=True,  null=True, default='', verbose_name= 'текст в кнопке ')
      def __str__(self):
        return "Слайд: %s" % (self.name)
      class Meta:
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"
