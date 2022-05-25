from django.shortcuts import render
from django.http import HttpResponse


def para(request,nr):
  print(request)
  print(nr)
  return HttpResponse("Die View para mit dem Parameter nr und dessen Wert " + str(nr))
  
def index(request):
    print(request)
    return HttpResponse("Die View index")