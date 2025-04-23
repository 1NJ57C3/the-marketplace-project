import pytest

from tests.utils import login_user, authenticate_client

@pytest.mark.django_db
def test_me_endpoint(api_client, create_user):
    create_user()
    login_resp = login_user(api_client)
    access = login_resp.data["tokens"]["access"]

    authenticate_client(api_client, access)

    resp = api_client.get("/api/users/me/")
    assert resp.status_code == 200
    assert resp.data["username"] == "testuser"
