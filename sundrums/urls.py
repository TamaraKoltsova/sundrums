from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from sundrums_admin.sitemaps import *
from django.contrib.sitemaps.views import sitemap
from sundrums_admin import views
#dicthonari for posts
sitemaps = {
    'posts' : Post_categoriesSitemap,
}



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('sundrums_admin.urls')),
    path('sitemap.xml',sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^posts/(?P<post_id>\w+)/', views.one_categories, name='posts'),
    url(r'^post_categories/(?P<post_id>\w+)/', views.one_categories, name='post_categories'),
    
    #тестирую ссылки первого уровня для переxода на главные ветки
   url(r'^magazin/$', views.tipe_posts_magazin, name='magazin'),
   url(r'^entsiklopediia/$', views.tipe_posts_entsiklopediia, name='entsiklopediia'),
   url(r'^novosti/$', views.tipe_posts_novosti, name='novosti'),
   url(r'^sobytiia/$', views.tipe_posts_sobytiia, name='sobytiia'),
   url(r'^korporativnye-treningi/$', views.tipe_posts_korporativnye_treningi, name='korporativnye-treningi'),
   url(r'^shkola/$', views.tipe_posts_shkola, name='shkola'),
   #тестирую ссылки первого уровня
   
   
   
   
   
    path(r'robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'),name='robots.txt'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'mailer/', include('mailer.urls', namespace='mailer')),
  
]\
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)