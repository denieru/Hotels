from rest_framework import viewsets
from .models import inih, menu, servh, archivo, habh 
from .serializer import inihSerializer, menuSerializer, servhSerializer, archSerializer,habhSerializer


class inihViewSet(viewsets.ModelViewSet):
    queryset = inih.objects.all()
    serializer_class = inihSerializer

class menuViewSet(viewsets.ModelViewSet):
    queryset = menu.objects.all()
    serializer_class = menuSerializer

class servhViewSet(viewsets.ModelViewSet):
    queryset = servh.objects.all()
    serializer_class = servhSerializer

class archViewSet(viewsets.ModelViewSet):
    queryset = archivo.objects.all()
    serializer_class = archSerializer

class habhViewSet(viewsets.ModelViewSet):
    queryset = habh.objects.all()
    serializer_class = habhSerializer
    
