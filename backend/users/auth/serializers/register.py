from django.contrib.auth import get_user_model
from rest_framework import serializers

from users.auth.utils import validate_password_confirmation


User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "confirm_password",
            "first_name",
            "last_name",
        ]
        read_only_fields = ["is_seller"]

    def validate(self, data):
        validate_password_confirmation(data["password"], data["confirm_password"])
        return data

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = User.objects.create_user(**validated_data)
        return user
