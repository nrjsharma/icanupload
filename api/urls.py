from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'download', views.ListDownload(), base_name="download")
urlpatterns = [
                   url(r'^show-download-list/', views.ListDownload.as_view(), name="show-download-list"),
              ]