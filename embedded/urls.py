from django.urls import re_path

import embedded.views

urlpatterns = [
    re_path(r'(?P<name>[a-z]+)$', embedded.views.url),
]
