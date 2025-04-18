from django.urls import path, include
from rest_framework import routers

from .views import UserRegisterView, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegisterView.as_view(), name='register'),
]

__all__ = ['urlpatterns']
