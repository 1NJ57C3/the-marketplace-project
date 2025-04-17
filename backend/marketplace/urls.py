"""
URL configuration for the Marketplace Django project.

Includes admin routes, DRF viewsets, and browsable API login/logout.
"""
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import get_user_model
from rest_framework import routers, serializers, viewsets

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_seller']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls)),
]
