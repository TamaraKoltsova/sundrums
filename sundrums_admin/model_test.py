from tinymce.models import HTMLField 
from django.db import models 
""" начало модели about_us """
class about_us(models.Model):
      name = models.CharField(&nbsp; &nbsp; &nbsp;max_length = 64, blank=True, &nbsp; null=True, default='None', verbose_name= ' ')
      description = HTMLField(&nbsp; &nbsp; &nbsp;&nbsp; blank=True, &nbsp; null=True, default='None', verbose_name='описание')
      icon = models.CharField(&nbsp; &nbsp; &nbsp;max_length = 64, blank=True, &nbsp; null=True, default='None', verbose_name='иконка с fontawesome.com')
      is_active = models.BooleanField(&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; default=True, verbose_name='добавить на главную?')
      def __str__(self):
        return "информаци€ о нас: %s" % (self.name)
      class Meta:
        verbose_name = "информаци€ о нас"
        verbose_name_plural = "информации"
""" начало модели Post_categories """
class Post_categories(models.Model):
      name = models.CharField(&nbsp; &nbsp; &nbsp;max_length = 64, blank=True, &nbsp; null=True, default='None', verbose_name= 'им€ категории в навигации ')
      description = HTMLField(&nbsp; &nbsp; &nbsp;&nbsp; blank=False, &nbsp; null=True, default='None', verbose_name= 'описание категории сюда можно поместить целую статью в html ')
      image = models.ImageField(&nbsp; &nbsp; &nbsp;blank=True, &nbsp; , upload_to='static/media/categories_images/', help_text = 'загрузите сюда изображение дл€ категории это будет в плитках навигации', &nbsp; verbose_name= ' главное изображение дл€ категории')
      is_active = models.BooleanField(&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; default='True', verbose_name= '¬кл? ')
      def __str__(self):
        return " атегори€: %s" % (self.name)
      class Meta:
        verbose_name = " атегори€"
        verbose_name_plural = " атегории"
