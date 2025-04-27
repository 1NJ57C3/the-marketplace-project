import pytest
from django.core import mail

from tests.utils import send_password_reset_email


@pytest.mark.django_db
def test_password_reset_request_sends_email(use_locmem_email_backend, api_client, create_user):
    """
    Given a user's email, request a reset and verify an email is sent.
    """
    # 1. Create user with known email and password
    create_user()

    # 2. Request password reset for that email
    email = "test@example.com"
    resp = send_password_reset_email(api_client, email)
    assert resp.status_code == 200

    # 3. Assert that the email was sent to the correct address
    assert len(mail.outbox) == 1
    assert email in mail.outbox[0].to
    #.TODO something like `assert {found_token} in mail.outbox[0].body`
