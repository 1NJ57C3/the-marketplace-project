from rest_framework import serializers


def validate_password_confirmation(
    password: str, password2: str, field_name="password"
) -> None:
    if password != password2:
        raise serializers.ValidationError({field_name: "Passwords must match."})
