from tinymce.models import HTMLField 
from django.db import models 
""" begin contact"""
class contact(models.Model):
      name = models.CharField(  max_length = 64, blank=True,  null=True, default='None', verbose_name= 'имя пользователя ')
      description = models.CharField(  max_length = 64, blank=True,  null=True, default='None', verbose_name= ' описание про пользователя ')
      is_active = models.BooleanField(   blank=True,  null=True, default='True', verbose_name= 'добавить контакты в ввыод на главную ')
      def __str__(self):
        return "контакт: %s" % (self.name)
      class Meta:
        verbose_name = "контакт"
        verbose_name_plural = "контакты"
