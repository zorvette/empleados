from django.contrib import admin
from .models import (
     Servicio,
     cliente,
     Ingrediente,
     Pedido,
     TipoDePago,
     Item
)


class ServicioAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'price', 'cliente', 'status'
    )
    list_filter = ('cliente',)
    search_fields = ('name', 'cliente__name')
    filter_horizontal = ('Ingrediente',)


class IngredienteAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'marca'
    )


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'direction', 'email', 'display_phone_number')

    def display_phone_number(self, obj):
            return obj.phone_number if obj.phone_number else '—'
    display_phone_number.short_description = 'Teléfono' 


class PedidoAdmin(admin.ModelAdmin):
     list_display = ('pk', 'name', 'cliente', 'date')
     list_filter = ('name',)


class ItemAdmin(admin.ModelAdmin):
     list_display = ( 'pedido', 'servicio', 'cant', 'observaciones')


# admin.site.register(Empleado)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(cliente, ContactAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(TipoDePago)
admin.site.register(Item, ItemAdmin)

