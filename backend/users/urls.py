from django.urls import path, include
from rest_framework import routers

from users.viewsets.users import UserViewSet
from users.views.me import MeView


# DRF ViewSets
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # ViewSet routes (automatically handled by router)
    path('', include(router.urls)),
    path('me/', MeView.as_view(), name='me'),
]

__all__ = ['urlpatterns']
