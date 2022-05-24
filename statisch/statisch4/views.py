from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('statisch4tpl.html')
    return HttpResponse(template.render())
