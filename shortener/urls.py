from django.urls import path, re_path
from django.contrib import admin

import shortener.views

urlpatterns = [
    path('add', shortener.views.AddUrlView.as_view(), name='add-url'),
    re_path(r'show/(?P<pk>[0-9a-f]{5,5})$', shortener.views.ShowUrlView.as_view(), name='show-url'),
    re_path(r'(?P<pk>[0-9a-f]{5,5})$', shortener.views.redirectUrl, name='redirect-url'),
]
