#from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse

from embedded.models import Url

def url(request, name):
    try:
        u = Url.objects.get(pk=name)
    except:
        return redirect(reverse("index"))
    return render(request, 'embedded/url.html', {'url': u})

