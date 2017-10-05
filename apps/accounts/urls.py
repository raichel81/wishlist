from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from . import views


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='main/')),
    url(r'^main/$', views.main, name='main'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]