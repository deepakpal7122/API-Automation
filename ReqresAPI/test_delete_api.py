import requests
import json

endpoint = "https://reqres.in/api/users/2"

def test_Delete_Request():
    response = requests.delete(endpoint)
    assert response.status_code == 204