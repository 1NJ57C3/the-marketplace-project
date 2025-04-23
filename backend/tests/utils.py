def login_user(api_client, username="testuser", password="strongpassword123"):
    return api_client.post("/api/auth/login/", {
        "username": username,
        "password": password,
    }, format="json")
