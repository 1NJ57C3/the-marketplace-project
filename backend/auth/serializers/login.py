from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom JWT login serializer that supports authentication via email or username.

    This override ensures SimpleJWT calls Django's `authenticate()` to engage
    custom backends, like FlexAuth.
    """

    def validate(self, attrs):
        """
        Attempt to authenticate the user using provided credentials.
        If successful, return basic user data with token pair.
        """
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(request=self.context.get('request'), username=username, password=password)

        if not user:
            raise serializers.ValidationError("No account found with the given credentials")
        

        self.user = user
        
        # generate tokens
        tokens = super().validate(attrs)

        # custom response data
        user_data = {
            "id": self.user.id,
            "username": self.user.username,
            "email": self.user.email,
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "is_seller": self.user.is_seller,
            "tokens": tokens,
        }
        return user_data
