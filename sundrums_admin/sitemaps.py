from django.contrib.sitemaps.views import sitemap
from  .models import *
#Post_categorie
#Posts

class PostsSitemap(sitemap):
    
    def items(self):
        return Posts.objects.all()