from rest_framework import serializers
from .models import *


class CommuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commune
        fields = '__all__'


class TypeLogementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeLogement
        fields = '__all__'


class QuartierSerializer(serializers.ModelSerializer):
    commune = CommuneSerializer(read_only=True, source='id_commune')

    class Meta:
        model = Quartier
        fields = '__all__'


class LogementSerializer(serializers.ModelSerializer):
    type = TypeLogementSerializer(read_only=True, source='type_logement')
    quartier = QuartierSerializer(read_only=True, source='id_quartier')

    class Meta:
        model = Logement
        fields = '__all__'


class IndividuSerializer(serializers.ModelSerializer):
    logement = LogementSerializer(read_only=True, source='num_logement')

    class Meta:
        model = Individu
        fields = '__all__'
