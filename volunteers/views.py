from rest_framework import viewsets
from .models import Voluntary
from .serializers import VoluntarySerializer


class VoluntaryViewSet(viewsets.ModelViewSet):
    queryset = Voluntary.objects.all()
    serializer_class = VoluntarySerializer
    authentication_classes = []
