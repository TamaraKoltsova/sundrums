from django.contrib.sitemaps.views import Sitemap
from  .models import *
#Post_categorie
#Posts

class PostsSitemap(Sitemap):
    
    def items(self):
        return Posts.objects.all()