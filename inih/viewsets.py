from rest_framework import viewsets
from .models import inih
from .serializer import inihSerializer


class inihViewSet(viewsets.ModelViewSet):
    queryset = inih.objects.all()
    serializer_class = inihSerializer
