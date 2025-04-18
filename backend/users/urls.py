from django.urls import path, include
from rest_framework import routers

from .viewsets.user import UserViewSet
from .views.auth import LogoutView, UserRegisterView

# DRF ViewSets
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    # ViewSet routes (automatically handled by router)
    path('', include(router.urls)),

    # Auth-related routes
    path('register/', UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

__all__ = ['urlpatterns']
