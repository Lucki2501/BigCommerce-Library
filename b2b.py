import requests
import init
from time import time
from utils import pr

def run():

    url = "https://api-b2b.bigcommerce.com/api/v3/io/addresses"

    body = {
  "companyId": 6034839,
  "firstName": "Sunil",
  "lastName": "Merchant",
  "companyName": "Sunny Components Inc",
  "addressLine1": "1370 E Cypress Street, Suite D",
  "addressLine2": "",
  "city": "West Covina",
  "stateName": "California",
  "country": "United States",
  "countryCode": "US",
  "zipCode": "91724",
  "phone": "+16269666259"
}

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "authToken": init.b2b_token
    }


    response = requests.post(url, json=body, headers=headers)
    print(response.status_code)
    return response.json()

def get():
    url = "https://api-b2b.bigcommerce.com/api/v3/io/users?companyId=2428553"
    
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "authToken": init.b2b_token
    }
    
    response = requests.get(url, headers=headers)
    
    return response.json()
