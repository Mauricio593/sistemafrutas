from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpleadosViewSet
# Crea un router y registra las vistas
router = DefaultRouter()
router.register(r'empleados', EmpleadosViewSet)

# Define las URLs de la API
urlpatterns = [
    path('', include(router.urls)),
]