from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class PhotoView(TemplateView):
    template_name ='base1.html'