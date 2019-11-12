from rest_framework import routers

from .viewsets import inihViewSet
router = routers.SimpleRouter()
router.register('inih', inihViewSet)
urlpatterns = router.urls 





'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio, name='Inicio'),
] '''
