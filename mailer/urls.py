from django.conf.urls import url, include
from . import views

app_name = 'mailer'

urlpatterns = [
    #url(r'^send_consultation', views.send_consultation, name='send_consultation'),
    url(r'^send_product', views.send_product, name='send_product'),
     #url(r'^send_product_spec', views.send_product_spec, name='send_product_spec'),
]
