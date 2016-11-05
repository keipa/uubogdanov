from django.conf.urls import url
# from django.contrib import admin
from teacher import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bootstrap/$', views.bootstrap, name='bootstrap'),
    url(r'^testing/$', views.testing, name='testing')
]
