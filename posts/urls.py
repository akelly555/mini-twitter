
from django.conf.urls import include, url
from django.contrib import admin
from posts import views
from users.views import (
	User_Register, User_Login,
)


urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^create$', views.create, name='create'),
	url(r'^(?P<pk>[\d]+)/update$', views.update, name='update'),
	url(r'^(?P<pk>[\d]+)/delete$', views.delete, name='delete'),
]

###  http://127.0.0.1:8000/






