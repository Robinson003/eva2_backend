from rest_framework.routers import DefaultRouter
from .api_views import ClienteViewSet, ProductoViewSet, VentaViewSet, DetalleVentaViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'detalleventas', DetalleVentaViewSet)

urlpatterns = router.urls
