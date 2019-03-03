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

