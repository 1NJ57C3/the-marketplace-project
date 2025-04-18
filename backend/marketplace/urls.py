"""
URL configuration for the Marketplace Django project.

Includes admin routes, browsable API auth, and registered DRF routes.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_fresh'),
    path('api/users/', include('users.urls')),
    path('api/auth/', include('users.auth.urls')),
]
