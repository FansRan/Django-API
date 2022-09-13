from rest_framework import viewsets
from .serializers import *


class CommuneViewSet(viewsets.ModelViewSet):
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializer


class TypeLogementViewSet(viewsets.ModelViewSet):
    queryset = TypeLogement.objects.all()
    serializer_class = TypeLogementSerializer


class QuartierViewSet(viewsets.ModelViewSet):
    queryset = Quartier.objects.all()
    serializer_class = QuartierSerializer


class LogementViewSet(viewsets.ModelViewSet):
    queryset = Logement.objects.all()
    serializer_class = LogementSerializer


class IndividuViewSet(viewsets.ModelViewSet):
    queryset = Individu.objects.all()
    serializer_class = IndividuSerializer
