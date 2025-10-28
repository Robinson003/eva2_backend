from django.contrib import admin
from .models import Cliente, Producto, Venta, DetalleVenta


class DetalleInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1


@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    inlines = [DetalleInline]


admin.site.register(Cliente)
admin.site.register(Producto)
# DetalleVenta no hace falta registrarlo por separado