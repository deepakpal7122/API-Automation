import requests
import json

endpoint = "https://reqres.in/api"

payload = {
    "name": "morpheus",
    "job": "zion resident"
}

def test_Put_Request():
    response = requests.put(endpoint + "/api/users/2", json=payload)
    assert response.status_code == 200
    
    json_response = json.loads(response.text)
    
    assert json_response.get("name") == "morpheus"