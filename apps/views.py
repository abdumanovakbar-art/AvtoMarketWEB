from django.shortcuts import render
from django.views.generic import ListView, TemplateView


# Create your views here.


class AvtoMarketViwe(TemplateView):
    template_name = 'base.html'


