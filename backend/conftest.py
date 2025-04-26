import pytest
from django.contrib.auth import get_user_model
from django.test import override_settings
from rest_framework.test import APIClient


User = get_user_model()


@pytest.fixture()
def use_locmem_email_backend():
    with override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'):
        yield


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user():
    def make_user(
        username="testuser",
        email="test@example.com",
        password="strongpassword123",
        **kwargs,
    ):
        defaults = {
            "username": username,
            "email": email,
            "password": password,
        }
        defaults.update(kwargs)
        return User.objects.create_user(**defaults)

    return make_user
