def login_user(api_client, username="testuser", password="strongpassword123"):
    return api_client.post("/api/auth/login/", {
        "username": username,
        "password": password,
    }, format="json")


def authenticate_client(api_client, token):
    """
    Sets the Authorization header on the given APIClient
    """
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")
    return api_client
