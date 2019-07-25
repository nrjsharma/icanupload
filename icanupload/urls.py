from django.contrib import admin
from django.urls import path
from django.conf.urls import (url, include)
from django.conf.urls.static import static
from django.conf import settings
from api import urls

urlpatterns = [
    path('superadmin/', admin.site.urls),
    url(r'^', include('dashboard.urls'), name='dashboard'),
    url(r'auth/', include('authuser.urls'), name='auth'),
    url(r'api/v1/', include(urls), name='api')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
