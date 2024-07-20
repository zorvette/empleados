from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

import datetime
# 
from applications.departamento.models import Departamento


class Empleado(models.Model):
    """ Modelo para tabla empleado """
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # avatar = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name


class cliente(models.Model):
    name = models.CharField('Nombre', max_length=50)
    direction = models.CharField('direccion', max_length=50)
    email = models.EmailField('E-mail', max_length=254)
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="El número de teléfono debe estar en el formato '+999999999' o '999999999'.",
            ),
        ],
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Ingrediente(models.Model):

    name = models.CharField('Nombre', max_length=20)
    marca = models.CharField('Marca', max_length=50, blank=True)

    def __str__(self):
        return self.name    


class Servicio(models.Model):
    name = models.CharField('Nombre', max_length=50)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    price = models.IntegerField('Precio')
    status = models.BooleanField('En el menu')
    Ingrediente = models.ManyToManyField(Ingrediente, related_name='hamburguesas')

    def __str__(self):
        return self.name + ' - ' + str(self.price)
    

class Pedido(models.Model):
    class status(models.TextChoices):
        PEDIDO = "pedido", _("Pedido")
        ESPERA = "espera", _("Espera")
        PAGADO = "pagado", _("Pagado")
        DEUDA = "deuda", _("Deuda")

    name = models.CharField('Status', max_length=6, choices=status.choices, default=status.PEDIDO)
    cliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    date = models.DateTimeField(_("Date"), auto_now_add=True)
    
    def __str__(self):
        return str(self.pk)


class TipoDePago(models.Model):
    class payment_type(models.TextChoices):
        EFECTIVO = "efectivo", _("Efectivo")
        NEQUI = "nequi", _("Nequi")
        DAVIPLATA = "daviplata", _("Daviplata")

    pago = models.CharField('Tipo', max_length=9, choices=payment_type.choices, default=payment_type.EFECTIVO)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    mount = models.IntegerField('Monto')
    
    def __str__(self):
        return self.pago
    
class Item(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    cant = models.IntegerField('Cantidad')
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return str(self.pedido.name)
