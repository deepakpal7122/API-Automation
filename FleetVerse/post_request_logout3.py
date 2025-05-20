import requests
import logging

logging.basicConfig(level=logging.INFO,format="%(asctime)s [%(levelname)s] - %(message)s")

def post_request_logout():
    url = "https://digital-osp-cv-dev-ms.api.tatamotors/api/v2/cv_online/logout/"
    auth_token = "DMBB6ErvwSF5K9hG7weJPUbIC7xOeL"
    
    headers = {"Authorization" : f"Bearer {auth_token}",
              "Content-Type" : "application/json"}
    
    try:
        response = requests.post(url, headers=headers, timeout=10)
        logging.info(f"Status code: {response.status_code}")
        
        assert response.status_code in [200, 204], f"Unexpected status code: {response.status_code}"
        logging.info("Logout POST request was successful.")
            
        if response.content:
            json_data = response.json()
            logging.info(f"Post Response JSON : {json_data}")
        
            # Basic check (optional)
            '''assert "userid" in json_data, "'userid' key not found in response"
            logging.info("'userid' found in response.")'''
                            
        else:
            logging.info("No JSON data content in response")
            
    except Exception as e:
        print("An error occured : ", e)

post_request_logout()
logging.info("............. Logout post request is Done............")
