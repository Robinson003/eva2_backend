from django.urls import path
from . import views

app_name = 'ventas'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    # LOGIN, LOGOUT y REGISTRO
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('registro/', views.registro_view, name='registro'),

    # CLIENTES
    path('clientes/', views.ClienteList.as_view(), name='clientes_list'),
    path('clientes/add/', views.ClienteCreate.as_view(), name='clientes_create'),
    path('clientes/<int:pk>/edit/', views.ClienteUpdate.as_view(), name='clientes_update'),
    path('clientes/<int:pk>/delete/', views.ClienteDelete.as_view(), name='clientes_delete'),

    # PRODUCTOS
    path('productos/', views.ProductoList.as_view(), name='productos_list'),
    path('productos/add/', views.ProductoCreate.as_view(), name='productos_create'),
    path('productos/<int:pk>/edit/', views.ProductoUpdate.as_view(), name='productos_update'),
    path('productos/<int:pk>/delete/', views.ProductoDelete.as_view(), name='productos_delete'),

    # VENTAS
    path('ventas/', views.VentaList.as_view(), name='ventas_list'),
    path('ventas/add/', views.VentaCreate.as_view(), name='ventas_create'),
    path('ventas/<int:pk>/edit/', views.VentaUpdate.as_view(), name='ventas_update'),
    path('ventas/<int:pk>/delete/', views.VentaDelete.as_view(), name='ventas_delete'),

    # DETALLE DE VENTAS
    path('detalleventas/', views.DetalleVentaList.as_view(), name='detalleventas_list'),
    path('detalleventas/add/', views.DetalleVentaCreate.as_view(), name='detalleventas_create'),
    path('detalleventas/<int:pk>/edit/', views.DetalleVentaUpdate.as_view(), name='detalleventas_update'),
    path('detalleventas/<int:pk>/delete/', views.DetalleVentaDelete.as_view(), name='detalleventas_delete'),
]