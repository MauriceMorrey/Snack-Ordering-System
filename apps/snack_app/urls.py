from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),  
    url(r'creat_or_join$', views.creat_or_join), 
]
