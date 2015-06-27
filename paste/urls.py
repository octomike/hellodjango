from django.conf.urls import include, url

import paste.views

urlpatterns = [
    url(r'^add/$', paste.views.AddCodeView.as_view(), name='add-code'),
    url(r'^(?P<pk>[0-9a-f]{5,5})$', paste.views.ShowCodeView.as_view(), name='show-code'),
]
