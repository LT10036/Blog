"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myblog.views import response,register,register2,login,login2
from myblog.tests import jsonss

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',response.as_view()),
    path('register',register),
    path('register2',register2),
    # path('ceshi',jsonss.as_view())
    path('login',login),
path('login2',login2),

]
