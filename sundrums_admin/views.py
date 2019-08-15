from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

from  .models import *
# обычная загрузка вида
def index(request):
    boss_say = helful_information.objects.get(english_name = 'boss_say')
    description_meta = helful_information.objects.get(english_name = 'description')
    keywords_meta = helful_information.objects.get(english_name = 'keywords')
    title_meta = helful_information.objects.get(english_name = 'title')
    contact_us = helful_information.objects.get(english_name = 'contact_us')
    logo = helful_information.objects.get(english_name = 'logo')
    adres = helful_information.objects.get(english_name = 'adres')
    telefon = helful_information.objects.get(english_name = 'telefon')
    email = helful_information.objects.get(english_name = 'email')
    teachers = teacher.objects.filter(is_active=True)
    topics = topic.objects.filter(is_active=True)
    Post_categoriess = Post_categories.objects.filter(is_active=True)
    sliders = slider.objects.filter(is_active=True)
    reviewss = reviews.objects.filter(is_active=True)
    socbuttons = socbutton.objects.filter(is_active=True)
    tipe_kurss = tipe_kurs.objects.filter(is_active=True)
    categories_product_mass = categories_product.objects.filter(is_active=True)
    return render(request, 'index.html', locals())#
    #

def one_categories(request, post_id):
    adres = helful_information.objects.get(english_name = 'adres')
    telefon = helful_information.objects.get(english_name = 'telefon')
    keywords_meta = helful_information.objects.get(english_name = 'keywords')
    email = helful_information.objects.get(english_name = 'email')
    description_meta = helful_information.objects.get(english_name = 'description')
    title_meta = helful_information.objects.get(english_name = 'title')
    teachers = teacher.objects.filter(is_active=True)
    topics = topic.objects.filter(is_active=True)
    sliders = slider.objects.filter(is_active=True)
    Post_categoriess = Post_categories.objects.filter(is_active=True)
    reviewss = reviews.objects.filter(is_active=True)
    Post_categories_one = Post_categories.objects.get(id = post_id)
    socbuttons = socbutton.objects.filter(is_active=True)
    tipe_kurss = tipe_kurs.objects.filter(is_active=True)
    return render(request, 'one_post.html', locals())#
    #
    
def one_post_simple(request, slug):
    adres = helful_information.objects.get(english_name = 'adres')
    telefon = helful_information.objects.get(english_name = 'telefon')
    keywords_meta = helful_information.objects.get(english_name = 'keywords')
    email = helful_information.objects.get(english_name = 'email')
    description_meta = helful_information.objects.get(english_name = 'description')
    title_meta = helful_information.objects.get(english_name = 'title')
    teachers = teacher.objects.filter(is_active=True)
    topics = topic.objects.filter(is_active=True)
    Post_categoriess = Post_categories.objects.filter(is_active=True)
    reviewss = reviews.objects.filter(is_active=True)
    #Post_one = Posts.objects.get(id = post_id)
    #id_for_categorie = Posts.objects.get(slug = slug)
    
    Post_one = get_object_or_404(Posts, slug=slug)
    print(  "номер такой"   ,Post_one.categories_id)
    name_for_categories= Post_categories.objects.get( id = int(Post_one.categories_3))
    socbuttons = socbutton.objects.filter(is_active=True)
    tipe_kurss = tipe_kurs.objects.filter(is_active=True)
    return render(request, 'one_post_simple.html', locals())#
    #
  

def tipe_posts(request, post_id):
    adres = helful_information.objects.get(english_name = 'adres')
    telefon = helful_information.objects.get(english_name = 'telefon')
    keywords_meta = helful_information.objects.get(english_name = 'keywords')
    email = helful_information.objects.get(english_name = 'email')
    description_meta = helful_information.objects.get(english_name = 'description')
    title_meta = helful_information.objects.get(english_name = 'title')
    topics = topic.objects.filter(is_active=True)
    teachers = teacher.objects.filter(is_active=True)
    sliders = slider.objects.filter(is_active=True)
    Post_categoriess = Post_categories.objects.filter(is_active=True)
    #Post_categories_tipe = Post_categories.objects.get(id = post_id)
    Post_categories_tipe = Posts.objects.filter(categories_id = post_id)
    reviewss = reviews.objects.filter(is_active=True)
    socbuttons = socbutton.objects.filter(is_active=True)
    tipe_kurss = tipe_kurs.objects.filter(is_active=True)
    return render(request, 'tipe_posts.html', locals())#
    #


def tipe_kurs_page(request, slug ):
    boss_say = helful_information.objects.get(english_name = 'boss_say')
    adres = helful_information.objects.get(english_name = 'adres')
    telefon = helful_information.objects.get(english_name = 'telefon')
    description_meta = helful_information.objects.get(english_name = 'description')
    keywords_meta = helful_information.objects.get(english_name = 'keywords')
    title_meta = helful_information.objects.get(english_name = 'title')
    email = helful_information.objects.get(english_name = 'email')
    teachers = teacher.objects.filter(is_active=True)
    topics = topic.objects.filter(is_active=True)
    Post_categoriess = Post_categories.objects.filter(is_active=True)
    sliders = slider.objects.filter(is_active=True)
    reviewss = reviews.objects.filter(is_active=True)
    socbuttons = socbutton.objects.filter(is_active=True)
    tipe_kurs_one=get_object_or_404(tipe_kurs, slug=slug)
    #tipe_kurs_one=tipe_kurs.objects.get(id =kurs_id)
    # получаем пароль и делаем защиту ввиде умножения на 3
    password_from_bd_for_kurs = int(tipe_kurs_one.password) * 3
    #print(password_from_bd_for_kurs)
    return render(request, 'tipe_kurs_page.html', locals())
    
def tipe_product_page(request, slug ):
    boss_say = helful_information.objects.get(english_name = 'boss_say')
    adres = helful_information.objects.get(english_name = 'adres')
    description_meta = helful_information.objects.get(english_name = 'description')
    keywords_meta = helful_information.objects.get(english_name = 'keywords')
    title_meta = helful_information.objects.get(english_name = 'title')
    telefon = helful_information.objects.get(english_name = 'telefon')
    email = helful_information.objects.get(english_name = 'email')
    teachers = teacher.objects.filter(is_active=True)
    topics = topic.objects.filter(is_active=True)
    Post_categoriess = Post_categories.objects.filter(is_active=True)
    sliders = slider.objects.filter(is_active=True)
    reviewss = reviews.objects.filter(is_active=True)
    socbuttons = socbutton.objects.filter(is_active=True)
    tipe_product_one=tipe_product.objects.get(slug = slug)
    return render(request, 'product_page_one.html', locals())    
  
'''  
def masseger(request):
    if request.method == "POST":
        from_form_name = request.POST["name"]
        from_form_email = request.POST["email"]
        from_form_tel = request.POST["tel"]
        from_form_masseger= request.POST["sms"]
        from_form_topic= request.POST["topic"]
        new_masseger= masseger( name = from_form_name, email = from_form_email,  tel = from_form_tel, sms = from_form_masseger, subject = from_form_topic)
        new_masseger.save()
        return HttpResponseRedirect("/") 
''' 

# для перевода на страницу с формой отправки
def contact_page(request):
    topics = topic.objects.filter(is_active=True)
    description_meta = helful_information.objects.get(english_name = 'description')
    keywords_meta = helful_information.objects.get(english_name = 'keywords')
    title_meta = helful_information.objects.get(english_name = 'title')
    return render(request, 'contact_page.html', locals())


def massegers(request):
    print('сообщение начало отправку')
    data = request.POST
    from_form_name = data.get("name")
    from_form_email = data.get("email")
    from_form_tel = data.get("tel")
    from_form_masseger= data.get("sms")
    from_form_topic= data.get("topic")
    new_masseger= masseger( name = from_form_name, mail = from_form_email,  tel = from_form_tel, sms = from_form_masseger, subject = from_form_topic)
    # проверка валидности reCAPTCHA
    if self.request.recaptcha_is_valid:
        new_masseger.save()
    #print("send!!!!!")
    return HttpResponse(u'Ваша заявка была отправлена')
    #return render(request, 'good_massege.html', locals())  
        
  
   
def img_load(request):
    img_load_mass = for_img_load.objects.filter(is_active=True)
    return render(request, 'img_page.html', locals())



""" 
тестовая ветка
"""
def tipe_posts_shkola(request):
    adres = helful_information.objects.get(english_name = 'adres')
    telefon = helful_information.objects.get(english_name = 'telefon')
    keywords_meta = helful_information.objects.get(english_name = 'keywords')
    email = helful_information.objects.get(english_name = 'email')
    description_meta = helful_information.objects.get(english_name = 'description')
    title_meta = helful_information.objects.get(english_name = 'title')
    topics = topic.objects.filter(is_active=True)
    teachers = teacher.objects.filter(is_active=True)
    sliders = slider.objects.filter(is_active=True)
    Post_categoriess = Post_categories.objects.filter(is_active=True)
    #Post_categories_tipe = Post_categories.objects.get(id = post_id)
    Post_categories_name = Post_categories.objects.get(id = 3)
    Post_categories_tipe = Posts.objects.filter(categories_id = 3)
    reviewss = reviews.objects.filter(is_active=True)
    socbuttons = socbutton.objects.filter(is_active=True)
    tipe_kurss = tipe_kurs.objects.filter(is_active=True)
    return render(request, 'tipe_posts.html', locals())#


def tipe_posts_magazin(request):
    adres = helful_information.objects.get(english_name = 'adres')
    telefon = helful_information.objects.get(english_name = 'telefon')
    keywords_meta = helful_information.objects.get(english_name = 'keywords')
    email = helful_information.objects.get(english_name = 'email')
    description_meta = helful_information.objects.get(english_name = 'description')
    title_meta = helful_information.objects.get(english_name = 'title')
    topics = topic.objects.filter(is_active=True)
    teachers = teacher.objects.filter(is_active=True)
    sliders = slider.objects.filter(is_active=True)
    Post_categoriess = Post_categories.objects.filter(is_active=True)
    #Post_categories_tipe = Post_categories.objects.get(id = post_id)
    Post_categories_tipe = Posts.objects.filter(categories_id = 8)
    Post_categories_name = Post_categories.objects.get(id = 8)
    reviewss = reviews.objects.filter(is_active=True)
    socbuttons = socbutton.objects.filter(is_active=True)
    tipe_kurss = tipe_kurs.objects.filter(is_active=True)
    return render(request, 'tipe_posts.html', locals())#


def tipe_posts_entsiklopediia(request):
    adres = helful_information.objects.get(english_name = 'adres')
    telefon = helful_information.objects.get(english_name = 'telefon')
    keywords_meta = helful_information.objects.get(english_name = 'keywords')
    email = helful_information.objects.get(english_name = 'email')
    description_meta = helful_information.objects.get(english_name = 'description')
    title_meta = helful_information.objects.get(english_name = 'title')
    topics = topic.objects.filter(is_active=True)
    teachers = teacher.objects.filter(is_active=True)
    sliders = slider.objects.filter(is_active=True)
    Post_categoriess = Post_categories.objects.filter(is_active=True)
    #Post_categories_tipe = Post_categories.objects.get(id = post_id)
    Post_categories_tipe = Posts.objects.filter(categories_id = 9)
    Post_categories_name = Post_categories.objects.get(id = 9)
    reviewss = reviews.objects.filter(is_active=True)
    socbuttons = socbutton.objects.filter(is_active=True)
    tipe_kurss = tipe_kurs.objects.filter(is_active=True)
    return render(request, 'tipe_posts.html', locals())#


def tipe_posts_novosti(request):
    adres = helful_information.objects.get(english_name = 'adres')
    telefon = helful_information.objects.get(english_name = 'telefon')
    keywords_meta = helful_information.objects.get(english_name = 'keywords')
    email = helful_information.objects.get(english_name = 'email')
    description_meta = helful_information.objects.get(english_name = 'description')
    title_meta = helful_information.objects.get(english_name = 'title')
    topics = topic.objects.filter(is_active=True)
    teachers = teacher.objects.filter(is_active=True)
    sliders = slider.objects.filter(is_active=True)
    Post_categoriess = Post_categories.objects.filter(is_active=True)
    #Post_categories_tipe = Post_categories.objects.get(id = post_id)
    Post_categories_tipe = Posts.objects.filter(categories_id = 6)
    Post_categories_name = Post_categories.objects.get(id = 6)
    reviewss = reviews.objects.filter(is_active=True)
    socbuttons = socbutton.objects.filter(is_active=True)
    tipe_kurss = tipe_kurs.objects.filter(is_active=True)
    return render(request, 'tipe_posts.html', locals())#
    
    
def tipe_posts_sobytiia(request):
    adres = helful_information.objects.get(english_name = 'adres')
    telefon = helful_information.objects.get(english_name = 'telefon')
    keywords_meta = helful_information.objects.get(english_name = 'keywords')
    email = helful_information.objects.get(english_name = 'email')
    description_meta = helful_information.objects.get(english_name = 'description')
    title_meta = helful_information.objects.get(english_name = 'title')
    topics = topic.objects.filter(is_active=True)
    teachers = teacher.objects.filter(is_active=True)
    sliders = slider.objects.filter(is_active=True)
    Post_categoriess = Post_categories.objects.filter(is_active=True)
    #Post_categories_tipe = Post_categories.objects.get(id = post_id)
    Post_categories_tipe = Posts.objects.filter(categories_id = 5)
    Post_categories_name = Post_categories.objects.get(id = 5)
    reviewss = reviews.objects.filter(is_active=True)
    socbuttons = socbutton.objects.filter(is_active=True)
    tipe_kurss = tipe_kurs.objects.filter(is_active=True)
    return render(request, 'tipe_posts.html', locals())# 
    
       
    
def tipe_posts_korporativnye_treningi(request):
    adres = helful_information.objects.get(english_name = 'adres')
    telefon = helful_information.objects.get(english_name = 'telefon')
    keywords_meta = helful_information.objects.get(english_name = 'keywords')
    email = helful_information.objects.get(english_name = 'email')
    description_meta = helful_information.objects.get(english_name = 'description')
    title_meta = helful_information.objects.get(english_name = 'title')
    topics = topic.objects.filter(is_active=True)
    teachers = teacher.objects.filter(is_active=True)
    sliders = slider.objects.filter(is_active=True)
    Post_categoriess = Post_categories.objects.filter(is_active=True)
    #Post_categories_tipe = Post_categories.objects.get(id = post_id)
    Post_categories_tipe = Posts.objects.filter(categories_id = 4)
    Post_categories_name = Post_categories.objects.get(id = 4)
    reviewss = reviews.objects.filter(is_active=True)
    socbuttons = socbutton.objects.filter(is_active=True)
    tipe_kurss = tipe_kurs.objects.filter(is_active=True)
    return render(request, 'tipe_posts.html', locals())# 