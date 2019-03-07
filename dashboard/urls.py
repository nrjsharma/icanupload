from django.conf.urls import url, include
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name="index"),
    url(r'^home/$', views.home, name="home")
]