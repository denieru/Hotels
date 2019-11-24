from rest_framework import routers
from .viewsets import inihViewSet, menuViewSet, servhViewSet, archViewSet,habhViewSet

router = routers.SimpleRouter()
router.register('Inicio', inihViewSet)
router.register('Menu', menuViewSet)
router.register('Servicios', servhViewSet)
router.register('Archivo', archViewSet)
router.register('Habitaciones', habhViewSet)
urlpatterns = router.urls 

