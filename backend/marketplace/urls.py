"""
URL configuration for the Marketplace Django project.

Includes admin routes, browsable API auth, and registered DRF routes.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('users.urls')),
]
