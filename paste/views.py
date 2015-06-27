from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import CreateView,DetailView
from django.core.urlresolvers import reverse

from paste.models import Code

class AddCodeView(CreateView):
    model = Code
    template_name = 'paste/add_code.html'
    fields = ['code']

    def get_context_data(self, **kwargs):
        context = super(AddCodeView,self).get_context_data(**kwargs)
        context['target'] = reverse('add-code')
        context['maxlength'] = self.model.pk
        return context

    def get_success_url(self):
        return reverse('show-code', kwargs={"pk": self.object.pk})

class ShowCodeView(DetailView):
    model = Code
    template_name = 'paste/show_code.html'
    fields = ['code']

