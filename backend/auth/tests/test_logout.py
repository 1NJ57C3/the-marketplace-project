import pytest

from tests.utils import login_user, authenticate_client, get_tokens, logout_user


@pytest.mark.django_db
def test_logout_blacklist_refresh(api_client, create_user):
    # Create & login
    create_user()
    login_resp = login_user(api_client)
    assert login_resp.status_code == 200

    access, refresh = get_tokens(login_resp)

    # Authenticate client for Logout
    authenticate_client(api_client, access)

    # Logout
    resp = logout_user(api_client, refresh)
    assert resp.status_code == 205

    # Attempt to refresh should now fail
    refresh_resp = api_client.post("/api/auth/login/refresh/", {
        "refresh": refresh
    }, format="json")
    assert refresh_resp.status_code == 401


@pytest.mark.django_db
def test_logout_requires_auth(api_client):
    # Attempt to log out without first being authenticated
    resp = logout_user(api_client, "I'vehadbetter,really")
    assert resp.status_code == 401
