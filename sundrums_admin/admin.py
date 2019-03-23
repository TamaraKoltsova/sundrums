from django.contrib import admin
from . models import *
# Register your models here.

''' для объедениения полей в админке'''
#class NoneInline(admin.TabularInline):
      #model = None
      #extra = 0

class massegerAdmin (admin.ModelAdmin):
      list_display = [field.name for field in masseger._meta.fields]
      #inlines = [NoneInline,]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = masseger

admin.site.register(masseger, massegerAdmin )

''' для объедениения полей в админке'''
#class NoneInline(admin.TabularInline):
      #model = None
      #extra = 0

class sliderAdmin (admin.ModelAdmin):
      list_display = [field.name for field in slider._meta.fields]
      #inlines = [NoneInline,]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = slider

admin.site.register(slider, sliderAdmin )

''' для объедениения полей в админке'''
class PostsInline(admin.TabularInline):
      model = Posts
      extra = 0

class Post_categoriesAdmin (admin.ModelAdmin):
      list_display = [field.name for field in Post_categories._meta.fields]
      inlines = [PostsInline,]
      #fields = []
      #exclude = []
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = Post_categories

admin.site.register(Post_categories, Post_categoriesAdmin )

''' для объедениения полей в админке'''
#class NoneInline(admin.TabularInline):
      #model = None
      #extra = 0

class PostsAdmin (admin.ModelAdmin):
      list_display = [field.name for field in Posts._meta.fields]
      #inlines = [NoneInline,]
      #fields = []
      exclude = ['categories']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = Posts

admin.site.register(Posts, PostsAdmin )

''' для объедениения полей в админке'''
class tipe_kursInline(admin.TabularInline):
      model = tipe_kurs
      extra = 0

class teacherAdmin (admin.ModelAdmin):
      list_display = [field.name for field in teacher._meta.fields]
      inlines = [tipe_kursInline,]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = teacher

admin.site.register(teacher, teacherAdmin )

''' для объедениения полей в админке'''
class apprenticeInline(admin.TabularInline):
      model = apprentice
      extra = 0
      
class kurs_videoInline(admin.TabularInline):
       model = kurs_video
       extra = 0

class tipe_kursAdmin (admin.ModelAdmin):
      list_display = [field.name for field in tipe_kurs._meta.fields]
      inlines = [apprenticeInline,kurs_videoInline]
      #fields = []
      #exclude = ['teacher_kurs']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = tipe_kurs

admin.site.register(tipe_kurs, tipe_kursAdmin )

''' для объедениения полей в админке'''
#class NoneInline(admin.TabularInline):
      #model = None
      #extra = 0

class apprenticeAdmin (admin.ModelAdmin):
      list_display = [field.name for field in apprentice._meta.fields]
      #inlines = [NoneInline,]
      #fields = []
      #exclude = ['kurs']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = apprentice

admin.site.register(apprentice, apprenticeAdmin )

''' для объедениения полей в админке'''
#class NoneInline(admin.TabularInline):
      #model = None
      #extra = 0

class helful_informationAdmin (admin.ModelAdmin):
      list_display = [field.name for field in helful_information._meta.fields]
      #inlines = [NoneInline,]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = helful_information

admin.site.register(helful_information, helful_informationAdmin )


class topicAdmin (admin.ModelAdmin):
      list_display = [field.name for field in topic._meta.fields]
      #inlines = [NoneInline,]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = topic

admin.site.register(topic, topicAdmin )


''' для объедениения полей в админке'''
#class NoneInline(admin.TabularInline):
      #model = None
      #extra = 0

class reviewsAdmin (admin.ModelAdmin):
      list_display = [field.name for field in reviews._meta.fields]
      #inlines = [NoneInline,]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = reviews

admin.site.register(reviews, reviewsAdmin )


''' Модель socbutton'''

class socbuttonAdmin (admin.ModelAdmin):
      list_display = [field.name for field in socbutton._meta.fields]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = socbutton

admin.site.register(socbutton, socbuttonAdmin )
''' конец Модели socbutton''' 


''' Модель kurs_video'''

class kurs_videoAdmin (admin.ModelAdmin):
      list_display = [field.name for field in kurs_video._meta.fields]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = kurs_video

admin.site.register(kurs_video, kurs_videoAdmin )
''' конец Модели kurs_video''' 

''' Модель categories_product'''
class tipe_productInline(admin.TabularInline):
       model = tipe_product
       extra = 0

class categories_productAdmin (admin.ModelAdmin):
      list_display = [field.name for field in categories_product._meta.fields]
      inlines = [tipe_productInline,]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = categories_product

admin.site.register(categories_product, categories_productAdmin )
''' конец Модели categories_product''' 

''' Модель tipe_product'''
class product_videoInline(admin.TabularInline):
       model = product_video
       extra = 0

class tipe_productAdmin (admin.ModelAdmin):
      list_display = [field.name for field in tipe_product._meta.fields]
      inlines = [product_videoInline,]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = tipe_product

admin.site.register(tipe_product, tipe_productAdmin )
''' конец Модели tipe_product''' 

''' Модель product_video'''

class product_videoAdmin (admin.ModelAdmin):
      list_display = [field.name for field in product_video._meta.fields]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = product_video

admin.site.register(product_video, product_videoAdmin )
''' конец Модели product_video''' 



''' Модель product_video'''

class for_img_loadAdmin (admin.ModelAdmin):
      list_display = [field.name for field in for_img_load._meta.fields]
      #fields = []
      #exclude = ['']
      #list_fields = ['']
      #searh_fields = ['']
      class Meta:
        model = for_img_load

admin.site.register(for_img_load, for_img_loadAdmin )
''' конец Модели product_video''' 
