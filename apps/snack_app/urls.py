from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),  
    url(r'join/(?P<id>[0-9a-zA-Z]+)?$', views.join), 
    url(r'new/?$', views.new), 
    
]
