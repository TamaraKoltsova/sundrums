from django.shortcuts import render
from . models import *
"""
def index(request):
      #sliders = slider.objects.filter(is_active=True)
      return render(request, 'index.html', locals())
"""




""" no param
def slider_view(request):
      #sliders = slider.objects.filter(is_active=True)
      return render(request, 'slider_page.html', locals())

"""

""" with param
def slider_view(request ,slider_id ):
      #sliders = slider.objects.get(id = slider_id)
      return render(request, 'slider_page.html', locals())

""" 
