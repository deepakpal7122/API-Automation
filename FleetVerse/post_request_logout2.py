import requests
import json

def post_request_logout():
    url = "https://digital-osp-cv-dev-ms.api.tatamotors/api/v2/cv_online/logout/"
    auth_token = "rG4v99nY02JKlg8UG3zZenLdf0l6Ab"
    headers = {"Authorization" : f"Bearer {auth_token}",
              "Content-Type" : "application/json"}
    
    try:
        response = requests.post(url, headers=headers)
        print("Status Code :", response.status_code)
        
        assert response.status_code == 201, f"Unexpected status code: {response.status_code}"
        print("Logout POST request was successful.")
            
        if response.content:
            json_data = response.json()
            print("Json Post Response body : ", json_data)
        
            # Basic check validation (optional) 
            '''assert "userid" in json_data, "'userid' key not found in response"
            print("'userid' found in response.")'''
                            
        else:
            print("No JSON content in response")
            
    except Exception as e:
        print("An error occured : ", e)

post_request_logout()
print("............. Logout post request is Done............")
