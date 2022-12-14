from django.shortcuts import render
from django.views.generic import TemplateView




class AboutPageView(TemplateView):
    template_name ='about.html'

# class SaytPageView(TemplateView):
#     template_name = 'sayt_nomi.html'
class basePageViwe(TemplateView):
    template_name = 'base.html'
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'
