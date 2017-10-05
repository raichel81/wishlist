from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^wish_items/(?P<pk>\d+)$', views.wish_items, name='wish_items'),
    url(r'^wish_items/create$', views.create, name='create'),
    url(r'^delete/(?P<pk>\d+)$', views.delete, name='delete'),
    url(r'^add/(?P<pk>\d+)$', views.add, name='add'),
    url(r'^remove/(?P<pk>\d+)$', views.remove, name='remove'),
]