from django.conf.urls import include, url

from django.contrib import admin
import django.contrib.auth.views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', django.contrib.auth.views.login),
    url(r'^accounts/logout/$', django.contrib.auth.views.logout),
    url(r'', include('blog.urls')),
]
