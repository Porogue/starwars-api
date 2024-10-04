from fastapi import FastAPI, HTTPException
import requests
import logging

SWAPI_BASE_URL = "https://swapi.dev/api/people/"

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/fetch")
def fetch_data():
    results = []
    id = 1

    logger.info("Starting fetch of the Star Wars characters from SWAPI.") 
    
    while True:
        try:
            url = f"{SWAPI_BASE_URL}{id}/"

            logger.info(f"Getting charactwer with ID {id}")

            response = requests.get(url)

            # Check if the status code of the response is not valid in order to break the loop
            if response.status_code == 404:
                logger.warning(f"ID {id} not found. End of the proccess.")
                break
            
            # If result is valid we append it
            if response.status_code == 200:
                character_data = response.json()
                results.append(character_data)
            else:
                logger.error(f"Error {response.status_code} getting data from the character with ID {url}")
                raise HTTPException(status_code=response.status_code, detail="Error from SWAPI")
            
        except requests.exceptions.RequestException as e:            
            logger.error(f"Error while trying to connect to SWAPI: {str(e)}")
            raise HTTPException(status_code=500, detail="Error connecting API")
        
        # Increase the counter
        id += 1
    
    # Sorting the result by name attribute
    sorted_results = sorted(results, key=lambda person: person['name'])

    logger.info(f"Characters have been stored")
        
    return {"people": sorted_results, "total": len(sorted_results)}