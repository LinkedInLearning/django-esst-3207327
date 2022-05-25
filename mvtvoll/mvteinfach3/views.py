from django.http import HttpResponse
from django.template import loader
from .models import Zitat

def index(request):
    sprueche = Zitat.zitate
    template = loader.get_template('mvteinfach3tpl.html')
    context = {
    'sprueche': sprueche,
    }
    return HttpResponse(template.render(context, request))