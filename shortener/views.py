from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView,DetailView
from django.views.generic.edit import ModelFormMixin
from django.core.urlresolvers import reverse

from shortener.models import Url

class AddUrlView(CreateView):
    model = Url
    template_name = 'shortener/add_url.html'
    fields = ['url']

    def get_context_data(self, **kwargs):
        context = super(AddUrlView,self).get_context_data(**kwargs)
        context['target'] = reverse('add-url')
        return context

    def form_valid(self, form):
        self.object = form.save()
        print(self.object.url)
        return super(ModelFormMixin, self).form_valid(form)

    def get_success_url(self):
        return reverse('show-url', kwargs={"pk": self.object.pk})

class ShowUrlView(DetailView):
    model = Url
    template_name = 'shortener/show_url.html'
    fields = ['url']


def redirectUrl(request, pk=None):
    return redirect(Url.objects.get(pk=pk).url)

def index(request):
    return render(request, 'index.html')
