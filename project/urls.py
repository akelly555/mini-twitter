"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from posts import views 
from users import views 
from django.conf.urls.static import static
from users.views import (
	User_Register, User_Login,
)

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^admin/', admin.site.urls),
	url(r'^posts/', include('posts.urls', namespace='posts')),
	url(r'^users/', include('users.urls',namespace='users')),
]


# urlpatterns = [
# 	# url(r'^$', views.index, name='home'),
# 	url(r'^register$', User_Register.as_view(), name='register'),
# 	url(r'^login$', User_Login.as_view(), name='login'),
# 	url(r'^create$', views.create, name='create'),
# 	url(r'^(?P<pk>[\d]+)/update$', views.update, name='update'),
# 	url(r'^(?P<pk>[\d]+)/delete$', views.delete, name='delete'),
# ]


###  http://127.0.0.1:8000/

