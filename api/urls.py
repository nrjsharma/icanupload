from django.conf.urls import url
from rest_framework import routers
from . import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'save-password', views.SavePasswordViewSet, base_name="save-password")  # NOQA
urlpatterns = [
                url(r'^show-download/', views.ListDownload.as_view(), name="show-download-list"),  # NOQA
              ]
urlpatterns += router.urls
