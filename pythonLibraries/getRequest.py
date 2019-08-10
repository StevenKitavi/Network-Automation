

#!/usr/bin/env python

#this is a complete python Script used to get 
#the interface configuration of a Cisco ASA

# Import Json so as to encode and decode json

import json
import requests
from requests.auth import HTTPBasicAuth

#this executes if our script is being run directly 
if __name__ == "__main__":
#An authentication object is created using the helper function
#called HTTPBasicAuth.
#works when the device supports basic authentication 
#auth is notably arbitary.all variables are.
    auth = HTTPBasicAuth('ntc', 'ntc123')

#statement creates a python dictionary for the http  request
#headers going to use in the API calls 
    headers ={
        'Accept' : 'application/json',
        'Content-Type' : 'application/json'
    }
#the url is is viewed as a varialbe called url to modularize our code  
#as also to simplify the response 
    url = "https://asav/api/interfaces/physical"
#do the api call executed using requests
    response = requests.get(url, auth=auth, headers=headers, verify=False)