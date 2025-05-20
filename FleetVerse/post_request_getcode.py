import requests
import logging

logging.basicConfig(level=logging.INFO,format="%(asctime)s [%(levelname)s] - %(message)s")

def post_request_getcode():
    url = "https://digital-osp-cv-dev-ms.api.tatamotors/api/v2/cv_online/send_otp/"
    auth_token = "meHNJ9qcrzkfBKzrhyIeZ3mBxzuctO"
    
    headers = {"Authorization" : f"Bearer {auth_token}",
              "Content-Type" : "application/json"}
    
    payload = {"mobile_number":"9850954869",
               "action_type":"login"}
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        logging.info(f"Status Code : {response.status_code}")
        
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        logging.info(f"Getcode post request was succesful.")
        
        if response.content:
            json_data = response.json()
            logging.info(f"Response JSON : {json_data}")
            
            msg = json_data["data"]["msg"]
            assert "Code sent" in msg, f"Code Sent message not found in response"
            logging.info("Code Sent Message is found in response") 
            logging.info("............ Get Code post request is Done ...........")
            
        else:
            logging.info(f"No JSON data content in response")
            
    except Exception as ex:
        logging.info(f"An error occured - {ex}")
        logging.error(f"Response body : {response.text}")
        logging.error("............. Get Code post request is Error............")

        
post_request_getcode()

