from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
   #url(r'^one_post/(?P<post_id>\w+)/', views.one_categories, name='one_post'),
   url(r'^tipe_posts/(?P<post_id>\w+)/', views.tipe_posts, name='tipe_posts'),
   
   #�������� ������ ������� ������
   url(r'^magazin/(?P<post_id>.+)/$', views.one_post_simple, name='magazin'),
   url(r'^entsiklopediia/(?P<post_id>.+)/$', views.one_post_simple, name='entsiklopediia'),
   url(r'^novosti/(?P<post_id>.+)/$', views.one_post_simple, name='novosti'),
   url(r'^sobytiia/(?P<post_id>.+)/$', views.one_post_simple, name='sobytiia'),
   url(r'^korporativnye-treningi/(?P<post_id>.+)/$', views.one_post_simple, name='korporativnye-treningi'),
   url(r'^shkola/(?P<post_id>.+)/$', views.one_post_simple, name='shkola'),
   #�������� ������ ������� ������
   
   
   #url(r'^one_post_simple/(?P<post_id>\w+)/', views.one_post_simple, name='one_post_simple'),
   url(r'^tipe_kurs_page/(?P<kurs_id>\w+)/', views.tipe_kurs_page, name='tipe_kurs_page'),
   url(r'^product_page/(?P<product_id>\w+)/', views.tipe_product_page, name='product_page'),
   url(r'^img/', views.img_load, name='img'),
   url(r'^massegers/', views.massegers, name='massegers'),
   
   url(r'contact_p/massegers/', views.massegers,),
   url(r'^contact_p/', views.contact_page, name='contact_p'),
   #url(r'^old/$', views.index, name='index'),
   ]
   
"""
magazin
entsiklopediia
novosti
sobytiia
korporativnye-treningi
shkola
"""