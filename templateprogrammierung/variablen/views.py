from django.http import HttpResponse
from django.template import loader
import random

def index(request):
    wert = random.randint(1,100)
    template = loader.get_template('variablentpl.html')
    context = {
    'zufallswert': wert,
    }
    return HttpResponse(template.render(context, request))