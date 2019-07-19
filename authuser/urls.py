from django.conf.urls import url
from authuser import views

urlpatterns = [
    url(r'^signup/$', views.SignUpView.as_view(), name="signup"),
    url(r'^login/$', views.LogInView.as_view(), name="login")
]
