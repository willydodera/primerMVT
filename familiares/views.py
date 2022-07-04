from django.http import HttpResponse
from django.template import loader
from familiares.models import Familiar

# Create your views here.
def familiar(self): 
    familiares = [
        Familiar(nombre='Milton', edad=40, fecha_nacimiento='1982-3-10'),
        Familiar(nombre='Boris', edad=36, fecha_nacimiento='1985-12-14'),
        Familiar(nombre='Horacio', edad=62, fecha_nacimiento='1959-10-29'),
        Familiar(nombre='Ana', edad=58, fecha_nacimiento='1963-07-12')
        ]
    
    for familiar in familiares:
        familiar.save()
    
    diccionario = {'lista':familiares}
    plantilla = loader.get_template("template.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
   

    