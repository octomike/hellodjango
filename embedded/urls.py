from django.conf.urls import url

import embedded.views

urlpatterns = [
    url(r'(?P<name>[a-z]+)$', embedded.views.url),
]
