from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('communes', CommuneViewSet, basename='communes')
router.register('type_logements', TypeLogementViewSet, basename='type_logements')
router.register('quartier', QuartierViewSet, basename='quartier')
router.register('logement', LogementViewSet, basename='logement')
router.register('individu', IndividuViewSet, basename='individu')

urlpatterns = [
    path('api/', include(router.urls))
]
