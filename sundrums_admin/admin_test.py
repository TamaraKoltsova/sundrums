from django.contrib import admin 
from . models import *

"""  Модель about_us """
class about_usAdmin (admin.ModelAdmin):
      list_display = [field.name for field in about_us._meta.fields]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = about_us
admin.site.register(about_us, about_usAdmin )
""" конец модели about_us"""

"""  Модель Post_categories """
class PostsInline(admin.TabularInline):
      model = Posts
      extra = 0

class Post_categoriesAdmin (admin.ModelAdmin):
      list_display = [field.name for field in Post_categories._meta.fields]
      inlines = [Posts,]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = Post_categories
admin.site.register(Post_categories, Post_categoriesAdmin )
""" конец модели Post_categories"""

