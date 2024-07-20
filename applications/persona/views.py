from django.shortcuts import render


from .models import Servicio



def servicio_usuario(request, usuario):
    servivio = Servicio.objects.filter(cliente__name__iexact=usuario)
    return render(request, 'home/servicio_por_usuario.html', {'hamburguesas': servivio, 'usuario': usuario})


