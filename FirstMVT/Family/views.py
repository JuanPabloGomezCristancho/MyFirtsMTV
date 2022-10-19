from django.shortcuts import render

from datetime import datetime
from django.template import loader
from django.http import HttpResponse
from Family.models import Relative

# Create your views here.
def create_relative(request, name, age, birthdate):

    birthdate = datetime.strptime(birthdate, '%Y-%m-%d')

    # Creacion del objeto y guardado en la base de datos.
    relative = Relative(name=name, age=age, birthdate=birthdate)
    relative.save()
    
    # Preparación para en render: template y diccionario.
    template = loader.get_template('family_template.html')
    dictionary = {"relative": relative}

    return HttpResponse(template.render(dictionary))

def relatives(request):
    relatives = Relative.objects.all()
    dictionary = {"relatives": relatives}
    return render(
        request=request,
        context=dictionary,
        template_name="Family/relative_list.html"
    )
