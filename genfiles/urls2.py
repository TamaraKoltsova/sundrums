from django.conf.urls import url, include
from . import views
urlpatterns = [
url(r'^$', views.index, name='index'),
#c параметром product_categ
#url(r'^product_categ_page/(?P<product_categ_id>\w+)/', views.product_categ_view, name='product_categ_page'),
#c параметром product_one
#url(r'^product_one_page/(?P<product_one_id>\w+)/', views.product_one_view, name='product_one_page'),
#c параметром type_work
#url(r'^type_work_page/(?P<type_work_id>\w+)/', views.type_work_view, name='type_work_page'),
#c параметром type_work_one
#url(r'^type_work_one_page/(?P<type_work_one_id>\w+)/', views.type_work_one_view, name='type_work_one_page'),
#без параметра product_categ
#url(r'^product_categ_page', views.product_categ_view, name='product_categ_page'),
#без параметра product_one
#url(r'^product_one_page', views.product_one_view, name='product_one_page'),
#без параметра type_work
#url(r'^type_work_page', views.type_work_view, name='type_work_page'),
#без параметра type_work_one
#url(r'^type_work_one_page', views.type_work_one_view, name='type_work_one_page'),
]
