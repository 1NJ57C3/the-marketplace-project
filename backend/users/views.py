from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets

from .serializers import UserSerializer, UserCreateSerializer

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
