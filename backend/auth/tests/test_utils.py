def assert_token_presence(response, expect_token=False):
    if expect_token:
        assert response.status_code == 200
        assert "access" in response.data['tokens'], "Expected access token in response"
        assert "refresh" in response.data['tokens'], "Expected refresh token in response"
    else:
        assert response.status_code == 401
        assert "access" in response.data['tokens'], "Did not expect access token in response"
        assert "refresh" in response.data['tokens'], "Did not expect refresh token in response"
