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
""" begin helful_information"""
class helful_information(models.Model):
      name =  models.CharField(  max_length = 64, blank=True,  null=True, default='', verbose_name= 'название')
      description =  HTMLField(   blank=True,  null=True, default='', verbose_name= 'описание полное если нужно ')
      english_name =  models.CharField(  max_length = 64, blank=True,  null=True, default='', verbose_name= 'английское название для фильтра ')
      is_active =  models.CharField(      default='True', verbose_name= 'вкл? ')
      text =  models.CharField(  max_length = 64, blank=True,  null=True, default='', verbose_name= 'просто текс')
      def __str__(self):
        return "полезная инф.: %s" % (self.name)
      class Meta:
        verbose_name = "полезная инф."
        verbose_name_plural = "полезная инф."
""" begin product_categ"""
class product_categ(models.Model):
      name =  models.CharField(  max_length = 64, blank=True,  null=True, default='', verbose_name= 'имя катеогрии')
      name_for_english =  models.CharField(  max_length = 64, blank=True,  null=True, default='', verbose_name= 'имя фильтра на английском например demontag')
      def __str__(self):
        return "фото работы: %s" % (self.name)
      class Meta:
        verbose_name = "фото работы"
        verbose_name_plural = "фото работ"
""" begin product_one"""
class product_one(models.Model):
      name =  models.CharField(  max_length = 64, blank=True,  null=True, default='', verbose_name= 'имя ')
      image =  models.ImageField(blank = True, upload_to='static/media/products_images/', help_text = '150x150px', verbose_name='Ссылка картники'       )
      description =  models.CharField(  max_length = 64, blank=True,  null=True, default='', verbose_name= 'описание')
      categories =  models.ForeignKey(product_categ, on_delete=models.SET_NULL, related_name = 'bag',  blank=True, null=True,       verbose_name= ' имя категории ')
      def __str__(self):
        return "фото: %s" % (self.name)
      class Meta:
        verbose_name = "фото"
        verbose_name_plural = "фото"
""" begin type_work"""
class type_work(models.Model):
      name =  models.CharField(  max_length = 164, blank=True,  null=True, default='', verbose_name= 'имя типа работ например демонтаж')
      image =  models.ImageField(blank = True, upload_to='static/media/work_img/', help_text = '150x150px', verbose_name='Ссылка картники',       verbose_name= 'картинка для вывода на главной очень маленькая 60Х60 ')
      desctioption1 =  models.CharField(  max_length = 2064, blank=True,  null=True, default='', verbose_name= 'описание в категория на главной')
      desctioption2 =  HTMLField(blank=True, null=True, default='' ,       verbose_name= 'описание уже самой работы можно копировать целые страницы html ')
      is_active =  models.BooleanField(default='True',       verbose_name= 'включить данную работу')
      kewords =  models.CharField(  max_length = 264, blank=True,  null=True, default='', verbose_name= ' keywords для seo  ')
      descriptions_seo =  models.CharField(  max_length = 264, blank=True,  null=True, default='', verbose_name= ' description для сео ')
      def __str__(self):
        return "тип работы: %s" % (self.name)
      class Meta:
        verbose_name = "тип работы"
        verbose_name_plural = "типы работ"
""" begin type_work_one"""
class type_work_one(models.Model):
      name =  models.CharField(  max_length = 2064, blank=True,  null=True, default='None', verbose_name= 'описание работы')
      text_for_info =  models.CharField(  max_length = 2064, blank=True,  null=True, default='None', verbose_name= 'текст если нужен в выпадающем меню')
      ed_izmerenia =  models.CharField(  max_length = 64, blank=True,  null=True, default='м2', verbose_name= 'единица измерения например м2')
      price =  models.CharField(  max_length = 64, blank=True,  null=True, default='', verbose_name= 'цена ')
      type_work =  models.ForeignKey(type_work, on_delete=models.SET_NULL, related_name = 'one', blank=True,  null=True, default='None',       verbose_name= 'связь с каким типом работ')
      is_active =  models.BooleanField(      default='True', verbose_name= 'включить для расчетов')
      kewords =  models.CharField(  max_length = 64, blank=True,  null=True, default='', verbose_name= 'ключевики сео ')
      description =  models.CharField(  max_length = 64, blank=True,  null=True, default='None', verbose_name= ' описание для сео ')
      def __str__(self):
        return "цена на одну работу: %s" % (self.name)
      class Meta:
        verbose_name = "цена на одну работу"
        verbose_name_plural = "цены на работу"
