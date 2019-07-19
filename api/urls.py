from django.conf.urls import url
from rest_framework import routers
from api import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'save-password', views.SavePasswordViewSet, base_name="save-password")  # NOQA
urlpatterns = [
    url(r'^show-download/', views.ShowDownloadView.as_view(), name="show-download-list"),  # NOQA
    url(r'^upload-file/', views.FileUploadView.as_view(), name="upload-file"),
    url(r'^signup/', views.SignUpUserView.as_view(), name="signup"),
    url(r'^login/', views.LoginView.as_view(), name="login"),
    url(r'^logout/', views.LogoutView.as_view(), name="logout"),

]
urlpatterns += router.urls
