from django.conf.urls import include, url
from django.contrib import admin

import shortener.views

urlpatterns = [
    url(r'^add/$', shortener.views.AddUrlView.as_view(), name='add-url'),
    url(r'^show/(?P<pk>[0-9a-f]{5,5})$', shortener.views.ShowUrlView.as_view(), name='show-url'),
    url(r'^(?P<pk>[0-9a-f]{5,5})$', shortener.views.redirectUrl, name='redirect-url'),
]
