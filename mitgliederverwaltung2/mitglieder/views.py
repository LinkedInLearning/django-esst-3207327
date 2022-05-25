from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .models import Mitglieder # Benötigt für die Daten des Modells - Version 3
from django.urls import reverse

def index(request):
    mitglieder = Mitglieder.objects.all().values()
    template = loader.get_template('main_template.html')
    context = {
        'mitglieder': mitglieder,
    }
    return HttpResponse(template.render(context, request))
