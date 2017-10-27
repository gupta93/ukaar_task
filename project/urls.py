from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^users/', include('register_app.urls')),
    url(r'', include('ukaar_blog.urls')),
]
