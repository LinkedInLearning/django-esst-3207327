from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    f = open("zitate.txt", "r")
    zitate = tuple(f.read())
    temp = "<ul>"
    for x in zitate:
        #temp += "<li>" + x + "</li>"
        temp += "<li>" + x + "</li>"
    temp += "</ul>"
    return HttpResponse(zitate)
