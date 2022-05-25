from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Zitat

def index(request):
    sprueche = Zitat.zitate
    output = ""
    for x in sprueche:
        output += x
    return HttpResponse(output)
