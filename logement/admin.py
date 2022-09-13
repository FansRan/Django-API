from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    list_filter = ('nom_commune', 'distance_agence', 'nbre_habitant')
    list_display = ('nom_commune', 'distance_agence', 'nbre_habitant')


@admin.register(TypeLogement)
class TypeLogementAdmin(admin.ModelAdmin):
    list_filter = ('type_logement', 'charges_forfaitaires')
    list_display = ('type_logement', 'charges_forfaitaires')


@admin.register(Quartier)
class QuartierAdmin(admin.ModelAdmin):
    list_filter = ('id_commune', 'libelle_quartier')
    list_display = ('id_commune', 'libelle_quartier')


@admin.register(Logement)
class LogementAdmin(admin.ModelAdmin):
    list_filter = ('type_logement', 'id_quartier', 'no', 'rue', 'superficie', 'loyer')
    list_display = ('type_logement', 'id_quartier', 'no', 'rue', 'superficie', 'loyer')


@admin.register(Individu)
class IndividuAdmin(admin.ModelAdmin):
    list_filter = ('num_logement', 'nom', 'prenom', 'date_naissance', 'num_telephone')
    list_display = ('num_logement', 'nom', 'prenom', 'date_naissance', 'num_telephone')
    list_display_links = ('num_logement',)
