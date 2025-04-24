import pytest

from tests.utils import login_user, authenticate_client, change_password, get_tokens, logout_user


@pytest.mark.django_db
def test_change_password(api_client, create_user):
    create_user()
    login_resp = login_user(api_client)

    access = get_tokens(login_resp, "access")
    authenticate_client(api_client, access)

    resp = change_password(api_client)
    assert resp.status_code == 200, "Expected successful password change"


@pytest.mark.django_db
def test_change_password_with_wrong_current(api_client, create_user):
    create_user()
    login_resp = login_user(api_client)

    access = get_tokens(login_resp, "access")
    authenticate_client(api_client, access)

    resp = change_password(api_client, old_password="wrong_password")
    assert resp.status_code == 400, "Expected unsuccessful password change"
    assert "old_password" in resp.data


@pytest.mark.django_db
def test_login_with_new_password(api_client, create_user):
    create_user()
    login_resp = login_user(api_client)

    access, refresh = get_tokens(login_resp)
    authenticate_client(api_client, access)

    new_password = "astrongerpassword123"
    change_password(api_client, new_password=new_password)
    logout_user(api_client, refresh)

    new_pw_resp = login_user(api_client, password=new_password)
    assert new_pw_resp.status_code == 200, "Expected successful login with new password"


@pytest.mark.django_db
def test_login_with_outdated_password(api_client, create_user):
    create_user()
    login_resp = login_user(api_client)

    access, refresh = get_tokens(login_resp)
    authenticate_client(api_client, access)

    old_password = "strongpassword123"
    new_pw_resp = change_password(api_client, old_password=old_password, new_password="anevenstrongerpassword123")
    assert new_pw_resp.status_code == 200, "Expected successful password change"
    logout_user(api_client, refresh)

    old_pw_resp = login_user(api_client, password=old_password)
    assert old_pw_resp.status_code == 400, "Expected unsuccessful login with old password"
