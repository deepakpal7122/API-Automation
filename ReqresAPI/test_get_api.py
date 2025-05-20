import requests
import json
import pytest

endpoint = "https://reqres.in/api/users/2"


def test_Get_APIEndpoint():
    response = requests.get(endpoint)
    print(f"Status Code: {response.status_code}")  # Print the status code
    assert response.status_code == 200  
    print(response.text)
    
    
# test_Get_APIEndpoint()