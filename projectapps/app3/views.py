from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hier ist die View-Funktion von app3")