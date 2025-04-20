import pytest


@pytest.mark.django_db
def test_login_with_username(api_client, create_user):
    create_user()
    response = api_client.post("api/auth/login", {
        "username": "testuser",
        "password": "strongpassword123",
    }, format="json")

    assert response.status_code == 200
    assert "access" in response.data or "token" in response.data
    assert "refresh" in response.data


@pytest.mark.django_db
def test_login_with_email(api_client, create_user):
    create_user()
    response = api_client.post("api/auth/login", {
        "username": "test@example.com",
        "password": "strongpassword123"
    }, format="json")

    assert response.status_code == 200
    assert "access" in response.data or "token" in response.data
    assert "refresh" in response.data
