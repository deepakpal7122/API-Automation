import requests
import logging
import json

logging.basicConfig(level=logging.INFO,format="%(asctime)s [%(levelname)s] - %(message)s")

def post_get_banner():
    url = "https://digital-osp-cv-dev-ms.api.tatamotors/api/v2/cv_online/admin/get_banner/"
    payload =   {
                "page": "HOME",
                "offset": 0,
                "size": 6,
                "source": ""
                }
    auth_token = "mvEh3eq3MTDYiY4l54tp5ZnwJviM5x"
    
    headers = {"Authorization" : f"Bearer {auth_token}",
               "Content-Type" : "application/json"}
    
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        logging.info(f"Status code : {response.status_code}")
        
        if response.status_code == 200:
            logging.info("'Get Banner' post request was successful.")
            
            if response.content:
                json_data = response.json()
                json_str = json.dumps(json_data, indent=4)
                logging.info(f"json response body : {json_str}")

                success_mesg = json_data.get("success", True)
                
                if success_mesg is True:
                    logging.info("'Success = true' found in response")
                    logging.info("............ Get Banner post request is Done ...........")
                else:
                    logging.error("'Success = true' not found in response body")
                    logging.error("............. Error Get Banner post request ............")
                
            else:
                logging.error("Response has no contain.")
                
        else:
            logging.error(f"Unexpected status code: {response.status_code}")
            logging.error(f"Response text: {response.text}")

    except Exception as ex:
        logging.exception(f"An error occurred : {ex}")
        

post_get_banner()
        