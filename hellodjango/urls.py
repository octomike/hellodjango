from django.contrib import admin
from django.urls import re_path, include

import shortener.views

urlpatterns = [
    re_path(r'^$', shortener.views.index, name='index'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^url/',   include('shortener.urls')),
    re_path(r'^paste/', include('paste.urls')),
    re_path(r'^embedded/', include('embedded.urls')),
]
