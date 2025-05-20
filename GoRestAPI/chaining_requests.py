import requests
import random
import json
import string

base_url = "https://gorest.co.in"
auth_token = "Bearer 27b4eeab91f63517c7025136d3321e37a60aa048c89238b50a0dc8c534e32d15"

# get random email id
def generate_random_email():
    domain = "gmail.com"
    email_length = 6
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(email_length))
    email = random_string + "@" + domain
    return email

# Get Request
def get_request():
    url = base_url + "/public/v2/users"
    print("get url: " + url)
    headers = {"Authorization" : auth_token}
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json get response body : ", json_str)
    print("............. Get user is Done............")



# Post Request
def post_request():
    url = base_url + "/public/v2/users"
    print("post url: " + url)
    headers = {"Authorization" : auth_token,
               'Accept' : 'application/json',
                
               }
    data = {
        "name": "Test",
        "email": generate_random_email(),
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url, json=data, headers=headers)
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json post response body : ", json_str)
    user_id = json_data["id"]
    print("user_id ==>", user_id)
    assert response.status_code == 201
    assert "name" in json_data
    assert json_data["name"] == "Test"
    print("............. Post user is Done............")
    return user_id



# Put Request
def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("put url: " + url)
    headers = {"Authorization" : auth_token}
    data = {
        "name": "Test testing",
        "gender": "male",
        "email": generate_random_email(),
        "status": "inactive"
        }

    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json put response body : ", json_str)
    assert json_data["id"] == user_id
    assert json_data["name"] == "Test testing"
    print("............. Put user is Done............")



# Delete Request
def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("delete url: " + url)
    headers = {"Authorization" : auth_token}
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print("............. Delete user is Done............")

get_request()
user_id = post_request()
put_request(user_id)
delete_request(user_id)