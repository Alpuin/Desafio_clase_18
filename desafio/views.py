from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from app_datos_f.models import Datos


def pagina_inicial(request):

    return HttpResponse("Inicio")


def pagina_segunda(request):

    return HttpResponse("Segunda pagina")


def plantilla_datos(
    self,
    dni: int = 0,
    nombre: str = 'nombre',
    apellido: str = 'apellido',
    agno: str = '1900-1-1'
    ):
    
    un_template = loader.get_template('template.html')

    datos = Datos(dni=dni, nombre=nombre, apellido=apellido, agno=agno)
    datos.save()
    
    un_context_dict = {
        'datos': datos
    }

    un_render = un_template.render(un_context_dict)

    return HttpResponse(un_render)
