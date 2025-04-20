import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


User = get_user_model()


@pytest.fixture
def api_client():
    APIClient


@pytest.fixture
def create_user():
    def make_user(**kwargs):
        defaults = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "strongpassword123",
        }
        defaults.update(kwargs)
        return User.objects.create_user(**defaults)

    return make_user
