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
        
        if response.status_code == 200:
            print("Logout POST request was successful.")
            
            if response.content:    
                json_data = response.json()
                json_str = json.dumps(json_data, indent=4)
                print("json get response body : ", json_str)
            
                # Basic check (optional)
                '''if "userid" in json_data:
                    print("Key userid found in response")
                else:
                    print("Key userid missing in response")'''
                    
            else:
                print("No JSON content in Post response body")  
                              
        else:
            print("Unexpected status code : ", response.status_code)
            print("Response text:", response.text)
            
    except Exception as ex:
        print("An error occured : ", ex)

post_request_logout()
print("............. Logout post request is Done............")
