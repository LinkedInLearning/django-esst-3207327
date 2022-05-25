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
  
def add(request):
  template = loader.get_template('add_template.html')
  return HttpResponse(template.render({}, request))

def addrecord(request):
  mitgliedneu = Mitglieder(mitgliedsnr= request.POST['mitgliedsnr'],vname=request.POST['vname'], 
  nname=request.POST['nname'], email=request.POST['email'])
  mitgliedneu.save()
  return HttpResponseRedirect(reverse('index'))  
def delete(request, mitgliedsnr):
  mitglied = Mitglieder.objects.get(mitgliedsnr=mitgliedsnr)
  mitglied.delete()
  return HttpResponseRedirect(reverse('index'))
  
def update(request, mitgliedsnr):
  mitglied = Mitglieder.objects.get(mitgliedsnr=mitgliedsnr)
  template = loader.get_template('update_template.html')
  context = {
    'mitglied': mitglied,
  }
  return HttpResponse(template.render(context, request))
  
def updaterecord(request, mitgliedsnr):
  mitglied = Mitglieder.objects.get(mitgliedsnr=mitgliedsnr)
 
 
  mitglied.mitgliedsnr = request.POST['mitgliedsnr']
  mitglied.vname=request.POST['vname']
  mitglied.nname=request.POST['nname']
  mitglied.email=request.POST['email']
  
  
  mitglied.save()
  return HttpResponseRedirect(reverse('index'))    
  