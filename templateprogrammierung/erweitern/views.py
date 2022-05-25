from django.http import HttpResponse
from django.template import loader
import random

def index(request):
    wert = random.randint(1,5)
    template = loader.get_template('subtpl.html')
    context = {
    'wert': wert,
    }
    return HttpResponse(template.render(context, request))