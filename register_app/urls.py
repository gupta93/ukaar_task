from django.conf.urls import url

from .views import signup


urlpatterns = [
    url(r'^signup/$', signup,name='signup'),
    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={'template_name': 'ukaar_blog/login.html'}
    ),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': '/'}
    ),
]
