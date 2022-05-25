from django.http import HttpResponse
from django.template import loader
import random

def index(request):
    werte = (random.randint(1,100),random.randint(1,100),random.randint(1,100))
    template = loader.get_template('einbindungtpl.html')
    context = {
    'werte': werte,
    }
    return HttpResponse(template.render(context, request))