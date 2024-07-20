
from django.contrib import admin
from django.urls import path
from applications.persona.views import servicio_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hamburguesas/user/<str:usuario>/', servicio_usuario, name='hamburguesas_por_usuario'),
    
]
