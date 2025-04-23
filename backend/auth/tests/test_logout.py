import pytest

from auth.tests.test_utils import login_user

@pytest.mark.django_db
def test_logout_blacklist_refresh(api_client, create_user):
    # Create & login
    create_user()
    login_resp = login_user(api_client)
    assert login_resp.status_code == 200

    access = login_resp.data["tokens"]["access"]
    refresh = login_resp.data["tokens"]["refresh"]

    # Authenticate client for Logout
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")

    # Logout
    resp = api_client.post("/api/auth/logout/", {
        "refresh": refresh
    }, format="json")
    assert resp.status_code == 205

    # Attempt to refresh should now fail
    refresh_resp = api_client.post("/api/auth/login/refresh/", {
        "refresh": refresh
    }, format="json")
    assert refresh_resp.status_code == 401

def test_logout_requires_auth(api_client):
    # Attempt to log out without first being authenticated
    resp = api_client.post("/api/auth/logout/", {
        "refresh": "I'vehadbetter,really"
    }, format="json")
    assert resp.status_code == 401
