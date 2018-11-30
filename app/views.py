from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from . import models
class IndexView(TemplateView):
    template_name = 'app/index.html'


# Create your views here.
