from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.models import User
from django.conf.urls import include

from Example1 import views

urlpatterns = [
    re_path(r'/example1/$',views.ExampleList.as_view()),
]