from rest_framework_simplejwt.views import TokenObtainPairView

from auth.serializers.login import CustomTokenObtainPairSerializer


class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
