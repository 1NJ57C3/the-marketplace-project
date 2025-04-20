from django.contrib.auth import get_user_model
from rest_framework import generics

from users.auth.serializers.register import UserCreateSerializer


User = get_user_model()

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
