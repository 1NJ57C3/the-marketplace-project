import pytest

from auth.tests.test_utils import login_user, assert_token_presence


@pytest.mark.django_db
def test_login_with_username(api_client, create_user):
    create_user()
    response = login_user(api_client)
    assert_token_presence(response, expect_token=True)


@pytest.mark.django_db
def test_login_with_email(api_client, create_user):
    create_user()
    response = login_user(api_client, username="test@example.com")
    assert_token_presence(response, expect_token=True)
