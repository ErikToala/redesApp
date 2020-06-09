from django.urls import re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets
from Login.views import CustonAuthToken

from Login import views

urlpatterns = [
    re_path(r'Login/$', CustonAuthToken.as_view()),
    re_path(r'example_login/$', views.LoginList2.as_view())

    #Hola soy Erik
]