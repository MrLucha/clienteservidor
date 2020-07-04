from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth.models import User
from django.conf.urls import include

from Example1 import views

urlpatterns = [
    re_path(r'/example1/$',views.ExampleList.as_view()),
    re_path(r'/example1_detail/(?P<id>\d+)/$',views.ExampleDetail.as_view()),
    re_path(r'/example1_update/(?P<id>\d+)/$',views.ExampleUpdate.as_view()),
    #re_path(r'/registro/$',views.Registro.as_view()),
]