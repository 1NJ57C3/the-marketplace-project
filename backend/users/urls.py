from django.urls import path, include
from rest_framework import routers

from .viewsets.user import UserViewSet

# DRF ViewSets
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # ViewSet routes (automatically handled by router)
    path('', include(router.urls)),
]

__all__ = ['urlpatterns']
