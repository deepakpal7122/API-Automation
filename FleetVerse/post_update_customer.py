import requests
import logging
import json

logging.basicConfig(level=logging.INFO,format="%(asctime)s [%(levelname)s] - %(message)s")

def post_update_customer():
    url = "https://digital-osp-cv-dev-ms.api.tatamotors/api/v2/cv_online/update_customer/"
    auth_token = "4NVhecgft18VfB5PFoZ4zOehKXMS9H"
    
    headers = {"Authorization" : f"Bearer {auth_token}",
               "Content-Type" : "application/json"}
    
    payload =  {
                "id": 3664,
                "last_name": "trtr",
                "email_id": "deepak.pal@vishleshan.net",
                "state": "Maharashtra",
                "district": "MUMBAI SUBURBAN",
                "address_one": "PalMH8109160706 trrrr",
                "account_type": "Individual",
                "first_name": "Deepak test"
                }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        logging.info(f"Status code : {response.status_code}")
        
        if response.status_code == 200:
            logging.info("'Update Customer' post request was successful.")
            
            if response.content:
                json_data = response.json()
                json_str = json.dumps(json_data, indent=4)
                logging.info(f"json response body : {json_str}")

                # success_mesg = json_data.get("success", True)
                msg = json_data["data"]["msg"]
                
                if "Data updated successfully." in msg:
                    logging.info("'Success = true' found in response")
                    logging.info("............ Update Customer post request is Done ...........")
                else:
                    logging.error("'Success = true' not found in response body")
                    logging.error("............. Error Update Customer post request ............")
                
            else:
                logging.error("Response has no contain.")
                
        else:
            logging.error(f"Unexpected status code: {response.status_code}")
            logging.error(f"Response text: {response.text}")

    except Exception as ex:
        logging.exception(f"An error occurred : {ex}")
        

post_update_customer()
        
        