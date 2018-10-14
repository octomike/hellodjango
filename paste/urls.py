from django.urls  import re_path, path

import paste.views

urlpatterns = [
    path('add', paste.views.AddCodeView.as_view(), name='add-code'),
    re_path(r'^(?P<pk>[0-9a-f]{5,5})$', paste.views.ShowCodeView.as_view(), name='show-code'),
]
