from django.shortcuts import render # benötigt beim Rendern
from django.http import HttpResponse
from django.template import loader # benötigt beim Laden eines Tempaltes
from .models import Mitglieder # Benötigt für die Daten des Modells

def index(request):
  mitglieder = Mitglieder.objects.all().values()
  output = "<table><tr><th>Mitgliedsnummer</th><th>Vorname</th><th>Nachname</th><th>E-Mail-Adresse</th></tr>"
  for x in mitglieder:
    output += "<tr><td>"  + str(x["mitgliedsnr"])+ "</td><td>" + x["vname"] + "</td><td>" + x["nname"] + "</td><td>" + x["email"] + "</td></tr>"
  output+="</table>"
  return HttpResponse(output)  