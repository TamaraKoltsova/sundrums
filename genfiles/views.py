from django.shortcuts import render
from . models import *

def index(request):
      #sliders = slider.objects.filter(is_active=True)
      #helful_informations = helful_information.objects.filter(is_active=True)
      #product_categs = product_categ.objects.filter(is_active=True)
      #product_ones = product_one.objects.filter(is_active=True)
      #type_works = type_work.objects.filter(is_active=True)
      #type_work_ones = type_work_one.objects.filter(is_active=True)
      return render(request, 'index.html', locals())





""" no param
def slider_view(request):
      #sliders = slider.objects.filter(is_active=True)
      return render(request, 'slider_page.html', locals())

def helful_information_view(request):
      #helful_informations = helful_information.objects.filter(is_active=True)
      return render(request, 'helful_information_page.html', locals())

def product_categ_view(request):
      #product_categs = product_categ.objects.filter(is_active=True)
      return render(request, 'product_categ_page.html', locals())

def product_one_view(request):
      #product_ones = product_one.objects.filter(is_active=True)
      return render(request, 'product_one_page.html', locals())

def type_work_view(request):
      #type_works = type_work.objects.filter(is_active=True)
      return render(request, 'type_work_page.html', locals())

def type_work_one_view(request):
      #type_work_ones = type_work_one.objects.filter(is_active=True)
      return render(request, 'type_work_one_page.html', locals())

"""

""" with param
def slider_view(request ,slider_id ):
      #sliders = slider.objects.get(id = slider_id)
      return render(request, 'slider_page.html', locals())

def product_categ_view(request ,product_categ_id ):
      #product_categs = product_categ.objects.get(id = product_categ_id)
      return render(request, 'product_categ_page.html', locals())

def product_one_view(request ,product_one_id ):
      #product_ones = product_one.objects.get(id = product_one_id)
      return render(request, 'product_one_page.html', locals())

def type_work_view(request ,type_work_id ):
      #type_works = type_work.objects.get(id = type_work_id)
      return render(request, 'type_work_page.html', locals())

def type_work_one_view(request ,type_work_one_id ):
      #type_work_ones = type_work_one.objects.get(id = type_work_one_id)
      return render(request, 'type_work_one_page.html', locals())

""" 
