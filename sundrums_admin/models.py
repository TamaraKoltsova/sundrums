from tinymce.models import HTMLField
from django.db import models
from uuslug import slugify  # Это библиотека для преобразования заголовков в ссылки django-uuslug

class masseger(models.Model):
      name = models.CharField(max_length = 64, blank=True,   null=True, default= ' ', verbose_name= ' ФИО' )
      subject = models.CharField(max_length = 64, blank=True,   null=True, default= ' ', verbose_name= 'тема сообщения ' )
      mail = models.CharField(max_length = 64, blank=True,   null=True, default= ' ', verbose_name= 'электронная почта ' )
      sms = models.CharField(max_length = 64, blank=True,   null=True, default= ' ', verbose_name= ' сообщение' )
      tel = models.CharField(max_length = 64, blank=True,   null=True, default= ' ', verbose_name= ' сообщение' )
      def __str__(self):
       return "сообщение: %s" % (self.name)
      class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

class slider(models.Model):
      name = models.CharField(      max_length = 64, blank=True,   null=True, default= ' ', verbose_name= ' имя слайда' )
      image = models.ImageField(      max_length = 64, blank=True, upload_to='sliders_images/', help_text = 'изображения для слайда',   default= ' ', verbose_name= 'путь к картинке' )
      description = models.CharField(      max_length = 250, blank=True,   null=True, default= ' ', verbose_name= ' описание или содержание слайда' )
      link = models.CharField(      max_length = 64, blank=True,   null=True, default='#featured-services', verbose_name= 'ссылка если нужна' )
      is_active = models.BooleanField(            null=True, default=True, verbose_name='добавить для вывода на основной странице?' )
      active_slide = models.CharField(      max_length = 16, blank=True,   null=True, default= ' ', verbose_name= 'активный ли это слайд (внимание написать active только для первого слайда в остальных случаях пустое значение) ' )
      button_text = models.CharField(      max_length = 64, blank=True,   null=True, default= ' ', verbose_name= 'текст кнопки' )
      
      def __str__(self):
       return "Слайд: %s" % (self.name)
      class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

class Post_categories(models.Model):
      name = models.CharField(      max_length = 64, blank=True,   null=True, default= ' ', verbose_name= 'имя категории в навигации ' )
      description = HTMLField(        blank=False,   null=True, default= ' ', verbose_name= 'описание категории сюда можно поместить целую статью в html ' )
      image = models.ImageField(      blank=True,    upload_to='static/media/categories_images/', help_text = 'загрузите сюда изображение для категории это будет в плитках навигации',   verbose_name= ' главное изображение для категории' )
      slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True)  # Поле для записи ссылки
      is_active = models.BooleanField(              default='True', verbose_name= 'Включить категорию на сайт? ' )
      def __str__(self):
       return "Категория: %s" % (self.name)
      class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
      
      def __str__(self):
        return self.name

      def __unicode__(self):
        return self.name
  
      def save(self):
        mass_for_slug = '{0}-{1}'.format(self.pk, slugify(self.name))  
        self.slug = mass_for_slug[2:]
        super(Post_categories, self).save()
class Posts(models.Model):
      name = models.CharField(      max_length = 255, blank=True,   null=True, default= ' ', verbose_name= 'имя статьи кратко это будет в меню навигации' )
      descrioptions_for_seo = models.CharField(      max_length = 264, blank=True,   null=True, default= ' ', verbose_name= 'h1 для сео' )
      descrioptions_for_title = models.CharField(      max_length = 264, blank=True,   null=True, default= ' ', verbose_name= 'title для сео' )
      descrioptions_for_descriptions = models.CharField(      max_length = 264, blank=True,   null=True, default= ' ', verbose_name= 'descriptions для сео' )
      description_for_main = models.CharField(      max_length = 255, blank=True,   null=True, default= ' ', verbose_name= 'описание для разделов на главной в плитках' )
      slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True)  # Поле для записи ссылки
      image = models.ImageField(      blank=True,    upload_to='static/media/post_images/', help_text = 'загрузите сюда изображение для категории это будет в плитках навигации',   verbose_name= ' главное изображение для отдельных статей' )
      description = HTMLField(      blank=True,   null=True, default= ' ', verbose_name= ' все описание статьи можно вставлять код html целиком' )
      categories = models.ForeignKey(Post_categories, on_delete=models.SET_NULL, related_name = 'post' ,  blank=True,   null=True, default= ' ', verbose_name= ' ' )
      is_active = models.BooleanField(              default='True', verbose_name= ' выложить статью на сайт ' )
      def __str__(self):
       return "Статья: %s" % (self.name)
      class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
      def __str__(self):
       return "Статья: %s" % (self.name)
      class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
      #'''  
      def __str__(self):
        return self.name

      def __unicode__(self):
        return self.name
  
      def save(self):
        #self.slug = '{0}-{1}'.format(self.pk, slugify(self.descrioptions_for_title))  # Статья будет отображаться в виде NN-АА-АААА
        mass_for_slug = '{0}-{1}'.format(self.pk, slugify(self.name))  # Статья будет отображаться в виде NN-АА-АААА
        self.slug = mass_for_slug[3:]
        super(Posts, self).save()
        #'''
class teacher(models.Model):
      name = models.CharField(      max_length = 64, blank=True,   null=True, default= ' ', verbose_name= 'ФИО ' )
      image = models.ImageField(      blank=True,    upload_to='static/media/post_images/', help_text = 'фото преподователя',   verbose_name=  'фото преподавателя' )
      tel = models.CharField(      max_length = 64, blank=True,   null=True, default= ' ', verbose_name= 'Номер телефона ' )
      email = models.CharField(      max_length = 64, blank=True,   null=True, default= ' ', verbose_name= 'адрес почты ' )
      info = models.CharField(      max_length = 64, blank=True,   null=True, default= ' ', verbose_name= 'информация об учителе ' )
      is_active = models.BooleanField(              default='True', verbose_name= 'Учитель работает ' )
      def __str__(self):
       return "Учитель: %s" % (self.name)
      class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

class tipe_kurs(models.Model):
      name = models.CharField(      max_length = 64, blank=True,   null=True, default= ' ', verbose_name= 'имя курса ' )
      info_kurs = HTMLField(        blank=True,   null=True, default= ' ', verbose_name= ' описание' )
      image = models.ImageField(      blank=True,    upload_to='static/media/kurs_images/', help_text = 'фото преподователя',   verbose_name=  'фото преподавателя' )
      slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True)  # Поле для записи ссылки
      teacher_kurs = models.ForeignKey(teacher, on_delete=models.SET_NULL, related_name = 'kurs',   null=True,         verbose_name= ' преподаватель' )
      password = models.CharField(      max_length = 64, blank=True,   null=True, default= '0', verbose_name= 'пароль для открытия статии (если оставить 0 то пароль запрашиваться не будет)) ' )
      
      is_active = models.BooleanField(              default='True', verbose_name= 'Курс активен?' )
      def __str__(self):
       return "Курс: %s" % (self.name)
      class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
      #'''  
      def __str__(self):
        return self.name

      def __unicode__(self):
        return self.name
  
      def save(self):
        #self.slug = '{0}-{1}'.format(self.pk, slugify(self.descrioptions_for_title))  # Статья будет отображаться в виде NN-АА-АААА
        mass_for_slug = '{0}-{1}'.format(self.pk, slugify(self.name))  # Статья будет отображаться в виде NN-АА-АААА
        self.slug = mass_for_slug[2:]
        super(Posts, self).save()
class apprentice(models.Model):
      name = models.CharField(      max_length = 64, blank=True,   null=True, default= ' ', verbose_name= ' ФИО' )
      tel = models.CharField(      max_length = 64, blank=True,   null=True, default= ' ', verbose_name= ' номер телефона' )
      email = models.CharField(      max_length = 64, blank=True,   null=True, default= ' ', verbose_name= ' email ' )
      info = models.CharField(      max_length = 164, blank=True,   null=True, default= ' ', verbose_name= 'информация об ученике если нужно' )
      kurs = models.ForeignKey(tipe_kurs, on_delete=models.SET_NULL, related_name = 'apprentice',       null=True,   verbose_name= 'здесь можно выбрать курс к которому прекрипить ученика' )
      is_active = models.BooleanField(              default='True', verbose_name= 'Активен ' )
      def __str__(self):
       return "Ученик: %s" % (self.name)
      class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'

class helful_information(models.Model):
      name = models.CharField(      max_length = 64, blank=True,   null=True, default= ' ', verbose_name= 'название' )
      description = HTMLField(        blank=True,   null=True, default= ' ', verbose_name= 'описание полное если нужно ' )
      english_name = models.CharField(      max_length = 64, blank=True,   null=True, default= ' ', verbose_name= 'английское название для фильтра ' )
      is_active = models.BooleanField(              default='True', verbose_name= 'вкл? ' )
      name_rus = models.CharField(      max_length = 64, blank=True,   null=True, default= ' ', verbose_name= 'имя на русском без html иногда нужно ' )
      def __str__(self):
       return "полезная инф.: %s" % (self.name)
      class Meta:
        verbose_name = 'полезная инф.'
        verbose_name_plural = 'полезная инф.'
class topic(models.Model):
      name = models.CharField(max_length = 64, blank=True,   null=True, default='', verbose_name= 'название темы для формы ' )
      is_active = models.BooleanField(default='True', verbose_name= 'вкл? ' )
      def __str__(self):
       return "тема для обратной связи: %s" % (self.name)
      class Meta:
        verbose_name = 'тема для обратной связи'
        verbose_name_plural = 'темы для обратной связи'
        
class reviews(models.Model):
      name = models.CharField(      max_length = 64, blank=True,   null=True, default='', verbose_name= ' фио кто оставил отзыв' )
      image = models.ImageField(      blank=True,    upload_to='static/media/reviews_images/', help_text = 'фото',   verbose_name=  'фото оставившего отзыв' )
      text_review = models.CharField(      max_length = 2054, blank=True,   null=True, default='', verbose_name= 'текст отзыва ' )
      prof_reviewrs = models.CharField(      max_length = 64, blank=True,   null=True, default='', verbose_name= 'профессия того кто оставил отзыв ' )
      is_active = models.BooleanField(              default='True', verbose_name= 'вкл? ' )
      def __str__(self):
       return "Отзыв: %s" % (self.name)
      class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'отзывы'
        
class socbutton(models.Model):
      name = models.CharField(max_length = 64, blank=True,   null=True, default='None', verbose_name= ' название' )
      link = models.CharField(max_length = 64, blank=True,   null=True, default='None', verbose_name= 'ссылка' )
      icon = models.CharField(max_length = 64, blank=True,   null=True, default='None', verbose_name= 'иконка с fontawesome.com ' )
      is_active = models.BooleanField(              default='True', verbose_name= 'вкл? ' )
      def __str__(self):
       return "соцкнопка: %s" % (self.name)
      class Meta:
        verbose_name = 'соцкнопка'
        verbose_name_plural = 'соцкнопки'  
        
class kurs_video(models.Model):
      name = models.CharField(max_length = 64, blank=True,   null=True, default='', verbose_name= 'имя видео' )
      video_link = models.CharField(max_length = 4064, blank=True,   null=True, default='', verbose_name= 'ссылка на видео из ютуба' )
      slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True)  # Поле для записи ссылки
      tipe_kurs = models.ForeignKey(tipe_kurs, on_delete=models.SET_NULL, related_name = 'postkurs',     null=True, default='', verbose_name= 'в какой курс добавлять' )
      text = HTMLField(                verbose_name= ' текст статьи поста ' )
      def __str__(self):
       return "статья с видео для курса: %s" % (self.name)
      class Meta:
        verbose_name = 'статья с видео для курса'
        verbose_name_plural = 'статьи с видео для курсов' 
        

class categories_product(models.Model):
      name = models.CharField(      max_length = 64, blank=True,   null=True, default= ' ', verbose_name= 'имя категории ' )
      name_ing = models.CharField(      max_length = 64, blank=True,   null=True, default= ' ', verbose_name= 'имя категории на английском для фильтра ' )
      slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True)  # Поле для записи ссылки
      is_active = models.BooleanField(              default='True', verbose_name= 'вкл?' )
      def __str__(self):
       return "категории товаров: %s" % (self.name)
      class Meta:
        verbose_name = 'категория товара'
        verbose_name_plural = 'категории товаров'  
    
class tipe_product(models.Model):
      name = models.CharField(      max_length = 64, blank=True,   null=True, default= ' ', verbose_name= 'имя товара ' )
      info_product = HTMLField(        blank=True,   null=True, default= ' ', verbose_name= ' описание' )
      slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True)  # Поле для записи ссылки
      image = models.ImageField(      blank=True,    upload_to='static/media/kproduct_images/', help_text = 'фото преподователя',   verbose_name=  'фото товара' )
      categories_product = models.ForeignKey(categories_product, on_delete=models.SET_NULL, related_name = 'product',   null=True,         verbose_name= 'категория товара' )
      #password = models.CharField(      max_length = 64, blank=True,   null=True, default= '0', verbose_name= 'пароль для открытия статии (если оставить 0 то пароль запрашиваться не будет)) ' )
      
      is_active = models.BooleanField(              default='True', verbose_name= 'вкл?' )
      def __str__(self):
       return "Товары: %s" % (self.name)
      class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'  
               
class product_video(models.Model):
      name = models.CharField(max_length = 64, blank=True,   null=True, default='', verbose_name= 'имя видео' )
      video_link = models.CharField(max_length = 64, blank=True,   null=True, default='', verbose_name= 'ссылка на видео из ютуба' )
      tipe_product = models.ForeignKey(tipe_product, on_delete=models.SET_NULL, related_name = 'postproduct',     null=True, default='', verbose_name= 'к какому продукту добавлять' )
      slug = models.CharField(verbose_name='Транслит', max_length=200, blank=True)  # Поле для записи ссылки
      text = HTMLField(                verbose_name= ' текст статьи поста ' )
      def __str__(self):
       return "статья с видео для товаров: %s" % (self.name)
      class Meta:
        verbose_name = 'статья с видео для товара'
        verbose_name_plural = 'статьи с видео для товара' 
        
class for_img_load(models.Model):
      name = models.CharField(      max_length = 64, blank=True,   null=True, default='', verbose_name= ' название картинки' )
      image = models.ImageField(      blank=True,    upload_to='static/media/reviews_images/', help_text = 'фото',   verbose_name=  'путь к картинке' )
      is_active = models.BooleanField(              default='True', verbose_name= 'вкл? ' )
      def __str__(self):
       return "картинки для загрузки в редактор: %s" % (self.name)
      class Meta:
        verbose_name = 'картинку для загрузки в редактор'
        verbose_name_plural = 'картинки для загрузки в редактор'                           