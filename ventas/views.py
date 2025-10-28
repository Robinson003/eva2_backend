from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Cliente, Producto, Venta, DetalleVenta
from django.db.models import Sum
import json

# ---------------- HOME ----------------
class HomeView(TemplateView):
    template_name = 'ventas/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # Top 5 productos más vendidos
        top_prod = DetalleVenta.objects.values('producto__nombre') \
                    .annotate(total_vendido=Sum('cantidad')) \
                    .order_by('-total_vendido')[:5]

        # Top 5 clientes con más compras
        top_clientes = Venta.objects.values('cliente__nombre') \
                        .annotate(total_ventas=Sum('total')) \
                        .order_by('-total_ventas')[:5]

        # Convertir Decimal a int para JSON
        ctx['top_prod'] = [{"producto__nombre": p['producto__nombre'], "total_vendido": int(p['total_vendido'] or 0)} for p in top_prod]
        ctx['top_clientes'] = [{"cliente__nombre": c['cliente__nombre'], "total_ventas": int(c['total_ventas'] or 0)} for c in top_clientes]

        # JSON para template
        ctx['top_prod_json'] = json.dumps(ctx['top_prod'])
        ctx['top_clientes_json'] = json.dumps(ctx['top_clientes'])

        return ctx

# ---------------- GENÉRICO CRUD ----------------
class GenericListView(ListView):
    template_name = 'ventas/list_generic.html'
    context_object_name = 'object_list'
    model_name = ''
    columns = []
    fields = []
    add_url = ''
    edit_url = ''
    delete_url = ''

    # NUEVO: campos numéricos
    numeric_fields = []

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.title
        ctx['model_name'] = self.model_name
        ctx['columns'] = self.columns
        ctx['fields'] = self.fields
        ctx['add_url'] = self.add_url
        ctx['edit_url'] = self.edit_url
        ctx['delete_url'] = self.delete_url
        ctx['numeric_fields'] = self.numeric_fields
        return ctx

# ---------------- GENÉRICO CRUD ----------------
class GenericCreateView(CreateView):
    template_name = 'ventas/form_generic.html'
    model_name = ''
    fields = []
    list_url = ''

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = f"➕ Nuevo {self.model_name}"
        ctx['model_name'] = self.model_name
        ctx['list_url'] = reverse_lazy(self.list_url)
        return ctx

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for visible in form.visible_fields():
            visible.field.widget.attrs['class'] = (
                'w-full border border-gray-300 rounded px-3 py-2 '
                'focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-green-500'
            )
        return form

class GenericUpdateView(UpdateView):
    template_name = 'ventas/form_generic.html'
    model_name = ''
    fields = []
    list_url = ''

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = f"✏️ Editar {self.model_name}"
        ctx['model_name'] = self.model_name
        ctx['list_url'] = reverse_lazy(self.list_url)
        return ctx

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for visible in form.visible_fields():
            visible.field.widget.attrs['class'] = (
                'w-full border border-gray-300 rounded px-3 py-2 '
                'focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-green-500'
            )
        return form

class GenericDeleteView(DeleteView):
    template_name = 'ventas/confirm_delete.html'
    model_name = ''
    list_url = ''

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['model_name'] = self.model_name
        ctx['list_url'] = reverse_lazy(self.list_url)
        return ctx

# ---------------- CLIENTES ----------------
class ClienteList(GenericListView):
    model = Cliente
    title = "👥 Clientes"
    model_name = "Cliente"
    columns = ["Nombre", "Email", "Teléfono"]
    fields = ["nombre", "email", "telefono"]
    add_url = 'ventas:clientes_create'
    edit_url = 'ventas:clientes_update'
    delete_url = 'ventas:clientes_delete'
    numeric_fields = []  # no hay campos numéricos

class ClienteCreate(GenericCreateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono']
    model_name = "Cliente"
    list_url = 'ventas:clientes_list'
    success_url = reverse_lazy('ventas:clientes_list')

class ClienteUpdate(GenericUpdateView):
    model = Cliente
    fields = ['nombre', 'email', 'telefono']
    model_name = "Cliente"
    list_url = 'ventas:clientes_list'
    success_url = reverse_lazy('ventas:clientes_list')

class ClienteDelete(GenericDeleteView):
    model = Cliente
    model_name = "Cliente"
    list_url = 'ventas:clientes_list'
    success_url = reverse_lazy('ventas:clientes_list')

# ---------------- PRODUCTOS ----------------
class ProductoList(GenericListView):
    model = Producto
    title = "🍏 Productos"
    model_name = "Producto"
    columns = ["Nombre", "Precio", "Stock"]
    fields = ["nombre", "precio", "stock"]
    add_url = 'ventas:productos_create'
    edit_url = 'ventas:productos_update'
    delete_url = 'ventas:productos_delete'
    numeric_fields = ["precio","stock"]

class ProductoCreate(GenericCreateView):
    model = Producto
    fields = ['nombre', 'precio', 'stock']
    model_name = "Producto"
    list_url = 'ventas:productos_list'
    success_url = reverse_lazy('ventas:productos_list')

class ProductoUpdate(GenericUpdateView):
    model = Producto
    fields = ['nombre', 'precio', 'stock']
    model_name = "Producto"
    list_url = 'ventas:productos_list'
    success_url = reverse_lazy('ventas:productos_list')

class ProductoDelete(GenericDeleteView):
    model = Producto
    model_name = "Producto"
    list_url = 'ventas:productos_list'
    success_url = reverse_lazy('ventas:productos_list')

# ---------------- VENTAS ----------------
class VentaList(GenericListView):
    model = Venta
    title = "🧾 Ventas"
    model_name = "Venta"
    columns = ["Cliente", "Total", "Fecha"]
    fields = ["cliente", "total", "fecha"]
    add_url = 'ventas:ventas_create'
    edit_url = 'ventas:ventas_update'
    delete_url = 'ventas:ventas_delete'
    numeric_fields = ["total"]

class VentaCreate(GenericCreateView):
    model = Venta
    fields = ['cliente', 'total', 'fecha']
    model_name = "Venta"
    list_url = 'ventas:ventas_list'
    success_url = reverse_lazy('ventas:ventas_list')

class VentaUpdate(GenericUpdateView):
    model = Venta
    fields = ['cliente', 'total', 'fecha']
    model_name = "Venta"
    list_url = 'ventas:ventas_list'
    success_url = reverse_lazy('ventas:ventas_list')

class VentaDelete(GenericDeleteView):
    model = Venta
    model_name = "Venta"
    list_url = 'ventas:ventas_list'
    success_url = reverse_lazy('ventas:ventas_list')

# ---------------- DETALLE VENTAS ----------------
class DetalleVentaList(GenericListView):
    model = DetalleVenta
    title = "📦 Detalle de Ventas"
    model_name = "DetalleVenta"
    columns = ["Venta", "Producto", "Cantidad"]
    fields = ["venta", "producto", "cantidad"]
    add_url = 'ventas:detalleventas_create'
    edit_url = 'ventas:detalleventas_update'
    delete_url = 'ventas:detalleventas_delete'
    numeric_fields = ["cantidad"]

class DetalleVentaCreate(GenericCreateView):
    model = DetalleVenta
    fields = ['venta', 'producto', 'cantidad']
    model_name = "DetalleVenta"
    list_url = 'ventas:detalleventas_list'
    success_url = reverse_lazy('ventas:detalleventas_list')

class DetalleVentaUpdate(GenericUpdateView):
    model = DetalleVenta
    fields = ['venta', 'producto', 'cantidad']
    model_name = "DetalleVenta"
    list_url = 'ventas:detalleventas_list'
    success_url = reverse_lazy('ventas:detalleventas_list')

class DetalleVentaDelete(GenericDeleteView):
    model = DetalleVenta
    model_name = "DetalleVenta"
    list_url = 'ventas:detalleventas_list'
    success_url = reverse_lazy('ventas:detalleventas_list')