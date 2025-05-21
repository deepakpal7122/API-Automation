import requests
import logging
import json

logging.basicConfig(level=logging.INFO,format="%(asctime)s [%(levelname)s] - %(message)s")

def post_request_verify_otp():
    url = "https://digital-osp-cv-dev-ms.api.tatamotors/api/v2/cv_online/verify_otp_v3/"
    auth_token = "DMBB6ErvwSF5K9hG7weJPUbIC7xOeL"
    
    headers = {"Authorization" : f"Bearer {auth_token}",
              "Content-Type" : "application/json"}
    
    payload = {"mobile_number":"9850954869",
               "otp_number":"123456"}
    
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        logging.info(f"Status Code : {response.status_code}")
        
        if response.status_code == 200:
            # logging.info(f"Expected Status code : 200" )
            logging.info("'Verify OTP' post request was successful.")
            
            if response.content:
                json_data = response.json()
                json_str = json.dumps(json_data, indent=4)
                print("json get response body : ", json_str)

                success_mesg = json_data.get("success", True)
                msg = json_data["success"]
                
                if success_mesg is True:
                    logging.info("'Success = true' found in response")
                    logging.info("............ Get Code post request is Done ...........")
                else:
                    logging.error("'Success = true' not found in response body")
                    logging.error("............. Error Get Code post request ............")
            
            else:
                logging.info("Response has no content..")
                
        else:
            logging.error(f"Unexpected status code: {response.status_code}")
            logging.error(f"Response text: {response.text}")
            
            
    except Exception as ex:
        logging.exception(f"An error occurred: {ex}")

        
post_request_verify_otp()


