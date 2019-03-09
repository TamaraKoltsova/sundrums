# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from .decorators import check_recaptcha
from sundrums_admin.models import *
from django.core.mail import send_mail


#verstalhiki@gmail.ru

def send_product(request):
    if request.recaptcha_is_valid:
        msg = ' %s \n    %s \n %s \n %s \n  %s \n  %s \n '%(request.POST['url'], request.POST['name'], request.POST['tel'], request.POST['email'], request.POST['topic'], request.POST['sms'])
        send_mail(u'Вам тестовое сообщение с сайта sundrums.ru', msg , settings.EMAIL_HOST_USER, ['Sundrums@mail.ru'], fail_silently=False)
    else:
        return HttpResponse(u'Пожайлуста пройдите проверку reCAPTCHA')        
    return HttpResponse(u'Ваша заявка была отправлена')
    
''''def send_product_spec(request):
    product = Product.objects.get(id=request.POST['product_id'])
    msg = 'Заявочка на продукт с адреса %s \n Имя: %s \n Телефон: %s \n Продукт: %s \n  в комплектации: %s \n  по цене %s'%(request.POST['url'], request.POST['first_name'], request.POST['phone'], product.name, request.POST['product_complect'], request.POST['product_complect_price'] )
    send_mail(u'Новая заявка', msg , settings.EMAIL_HOST_USER, ['verstalhiki@gmail.ru'], fail_silently=False)    
    return HttpResponse(u'Ваша заявка была отправлена')'''

