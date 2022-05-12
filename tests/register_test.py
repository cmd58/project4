"""This tests the registration"""

def test_auth_pages(client):
    response = client.get("/register")
    assert response.status_code == 200
