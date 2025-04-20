from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.auth.utils import validate_password_confirmation


User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name']
        read_only_fields = ['is_seller']

    def validate(self, data):
        validate_password_confirmation(data['password'], data['password2'])
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
