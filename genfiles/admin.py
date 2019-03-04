from django.contrib import admin 
from . models import *

"""  Модель slider """
class sliderAdmin (admin.ModelAdmin):
      list_display = [field.name for field in slider._meta.fields]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = slider
admin.site.register(slider, sliderAdmin )
""" конец модели slider"""

"""  Модель helful_information """
class helful_informationAdmin (admin.ModelAdmin):
      list_display = [field.name for field in helful_information._meta.fields]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = helful_information
admin.site.register(helful_information, helful_informationAdmin )
""" конец модели helful_information"""

"""  Модель product_categ """
class product_oneInline(admin.TabularInline):
      model = product_one
      extra = 0

class product_categAdmin (admin.ModelAdmin):
      list_display = [field.name for field in product_categ._meta.fields]
      inlines = [product_oneInline,]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = product_categ
admin.site.register(product_categ, product_categAdmin )
""" конец модели product_categ"""

"""  Модель product_one """
class product_oneAdmin (admin.ModelAdmin):
      list_display = [field.name for field in product_one._meta.fields]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = product_one
admin.site.register(product_one, product_oneAdmin )
""" конец модели product_one"""

"""  Модель type_work """
class type_work_oneInline(admin.TabularInline):
      model = type_work_one
      extra = 0

class type_workAdmin (admin.ModelAdmin):
      list_display = [field.name for field in type_work._meta.fields]
      inlines = [type_work_oneInline,]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = type_work
admin.site.register(type_work, type_workAdmin )
""" конец модели type_work"""

"""  Модель type_work_one """
class type_work_oneAdmin (admin.ModelAdmin):
      list_display = [field.name for field in type_work_one._meta.fields]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = type_work_one
admin.site.register(type_work_one, type_work_oneAdmin )
""" конец модели type_work_one"""

