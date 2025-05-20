import requests
import json

payload = {
        "name": "Deepak",
        "job": "Tester"
        }   

endpoint = "https://reqres.in/api/users"

def test_Post_Request():
    response = requests.post(endpoint, json=payload)
    assert response.status_code == 201
    json_response = json.loads(response.text)
    
    Id = json_response["id"]
    if "id" in json_response:
        print("Id found - ", Id)
    else:
        print("id not found")
        
    assert response.json()["name"] == "Deepak"
    assert json_response.get("name") == "Deepak"