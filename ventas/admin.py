
from django.contrib import admin
from .models import Cliente, Pedido


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "limite_credito_clp")
    list_filter = ("apellido",)
    search_fields = ("nombre", "apellido", "email")

    @admin.display(description="Límite de crédito")
    def limite_credito_clp(self, obj):
        return f"${obj.limite_credito:,.0f}".replace(",", ".")


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("cliente", "descripcion", "fecha", "total_clp", "estado")
    list_filter = ("estado", "fecha")
    search_fields = ("cliente__nombre", "cliente__apellido", "descripcion")

    @admin.display(description="Total")
    def total_clp(self, obj):
        return f"${obj.total:,.0f}".replace(",", ".")
