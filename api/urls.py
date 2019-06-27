from django.conf.urls import url
from rest_framework import routers
from . import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'save-password', views.SavePasswordViewSet, base_name="save-password")  # NOQA
urlpatterns = [
                url(r'^show-download/', views.ListDownloadAPIView.as_view(), name="show-download-list"),  # NOQA
                url(r'^upload-file/', views.FileUploadAPIView.as_view(), name="upload-file"),  # NOQA
              ]
urlpatterns += router.urls
