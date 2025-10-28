from .models import Producto, Cliente, Venta, DetalleVenta
from django.utils import timezone
import random

# --------------------------
# Limpiar productos antiguos
# --------------------------
Producto.objects.exclude(nombre__in=['Manzana','Plátano','Naranja','Fresa','Uva','Mango']).delete()

# --------------------------
# Crear productos de frutas
# --------------------------
frutas = [
    {'nombre':'Manzana','precio':1200},
    {'nombre':'Plátano','precio':800},
    {'nombre':'Naranja','precio':1000},
    {'nombre':'Fresa','precio':1500},
    {'nombre':'Uva','precio':2000},
    {'nombre':'Mango','precio':2500},
]

for fruta in frutas:
    Producto.objects.update_or_create(
        nombre=fruta['nombre'],
        defaults={'precio': fruta['precio'], 'stock': random.randint(10,50)}
    )

# --------------------------
# Crear clientes ejemplo
# --------------------------
clientes = ['Robinson', 'María', 'Juan', 'Luisa', 'Carlos']
for c in clientes:
    Cliente.objects.update_or_create(
        nombre=c,
        defaults={'email': f"{c.lower()}@mail.com", 'telefono': '123456789'}
    )

# --------------------------
# Crear ventas y detalle de ventas
# --------------------------
productos = list(Producto.objects.all())
clientes_objs = list(Cliente.objects.all())

# Limpiar ventas anteriores
DetalleVenta.objects.all().delete()
Venta.objects.all().delete()

for _ in range(20):
    cliente = random.choice(clientes_objs)
    venta = Venta.objects.create(cliente=cliente, total=0, fecha=timezone.now())
    total = 0
    for _ in range(random.randint(1,3)):
        producto = random.choice(productos)
        cantidad = random.randint(1,5)
        DetalleVenta.objects.create(venta=venta, producto=producto, cantidad=cantidad)
        total += producto.precio * cantidad
    venta.total = total
    venta.save()
