from django.conf.urls import include, url
from django.contrib import admin

import shortener.views
import shortener.urls
import paste.urls

urlpatterns = [
    url(r'^$', shortener.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^url/', include(shortener.urls)),
    url(r'^paste/', include('paste.urls')),
]
