from django.contrib import admin 
from . models import *

"""  Модель contact """
class contactAdmin (admin.ModelAdmin):
      list_display = [field.name for field in contact._meta.fields]
      #fields = []
      #exclude = []
      #list_fields = []
      #searh_fields = []
      class Meta:
        model = contact
admin.site.register(contact, contactAdmin )
""" конец модели contact"""

