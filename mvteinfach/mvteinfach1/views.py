from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Zitat

def index(request):
    template = loader.get_template('mvteinfach1tpl.html')
    return HttpResponse(template.render())
