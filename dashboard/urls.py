from django.conf.urls import url
from django.urls import path
from dashboard import views
urlpatterns = [
    path('', views.DashboardView.as_view(), name="index"),
    url(r'^home/$', views.DashboardView.as_view(), name="home")
]
