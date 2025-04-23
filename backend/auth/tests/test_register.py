import pytest


@pytest.mark.django_db
def test_user_registration(api_client):
    data = {
        "username": "newuser",
        "email": "new@example.com",
        "password": "strongpassword123",
        "confirm_password": "strongpassword123",
    }
    resp = api_client.post("/api/auth/register/", data, format="json")
    assert resp.status_code == 201
    assert "id" in resp.data
