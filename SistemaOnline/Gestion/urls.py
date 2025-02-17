from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpleadosViewSet,clientesViewSet,productosViewSet
# Crea un router y registra las vistas
router = DefaultRouter()
router.register(r'empleados', EmpleadosViewSet)
router.register(r'clientes', clientesViewSet)
router.register(r'productos', productosViewSet)
# Define las URLs de la API
urlpatterns = [
    path('', include(router.urls)),
]


