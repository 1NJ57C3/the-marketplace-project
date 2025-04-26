from rest_framework.test import APIClient
from django.core.handlers.wsgi import WSGIRequest

def login_user(api_client: APIClient, username="testuser", password="strongpassword123"):
    return api_client.post("/api/auth/login/", {
        "username": username,
        "password": password,
    }, format="json")


def authenticate_client(api_client: APIClient, token: str):
    """
    Sets the Authorization header on the given APIClient.
    """
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client


def logout_user(api_client: APIClient, refresh_token: str):
    return api_client.post("/api/auth/logout/", {
        "refresh": refresh_token,
    }, format="json")


def change_password(api_client: APIClient, old_password="strongpassword123", new_password="strongerpassword123"):
    return api_client.post("/api/auth/change-password/", {
        "old_password": old_password,
        "new_password": new_password,
        "confirm_password": new_password,
    }, format="json")


def get_tokens(response: WSGIRequest, token="pair"):
    """
    Retrieve JWT token(s) from a login response.

    Args:
        response: DRF Response with .data["tokens"] dict.
        token: One of "access", "refresh", or "pair".

    Returns:
        If "pair", returns (access, refresh).
        If "access" or "refresh", returns that single token.

    Raises:
        ValueError: If `token` is not one of the expected values.

    """
    tokens = response.data.get("tokens", {})
    if token == "pair":
        return tokens["access"], tokens["refresh"]
    elif token == "access":
        return tokens["access"]
    elif token == "refresh":
        return tokens["refresh"]
    raise ValueError('Token argument must be "access", "refresh", "pair"')


def send_password_reset_email(api_client: APIClient, email="test@example.com"):
    """Request a password reset email."""
    return api_client.post("/api/auth/password-reset/", {
        "email": email,
    }, format="json")
