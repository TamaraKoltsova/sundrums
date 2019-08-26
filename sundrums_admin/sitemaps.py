from django.contrib.sitemaps import Sitemap
from  .models import *
#Post_categorie
#Posts



class PostsSitemap(Sitemap):
    
    def items(self):
        return Posts.objects.all()
   

class Post_categoriesSitemap(Sitemap):
    
    def items(self):
        return Post_categories.objects.all() 
       
class tipe_productSitemap(Sitemap):
    
    def items(self):
        return tipe_product.objects.all() 
        
        
class tipe_kursSitemap(Sitemap):
    
    def items(self):
        return tipe_kurs.objects.all() 
                
        
        
       
                      