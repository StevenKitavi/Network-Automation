#Sample python script which makes an api call
#  to execute the show version command
import json
import requests
from requests.auth import HTTPBasicAuth

#this part of the script parameterizes the Credentials,headers 
# and url required to use NX-API
#this executes if our script is being run directly 
if __name__ == "__main__":
    auth = HTTPBasicAuth('ntc' , 'ntc123')
    headers = {
        "Content-Type" : 'application/json',
        'Accept' : 'application/json'
    }
    url = 'http://nxos-spine1/ins'

    payload = {
        "ins_api" : {
            "version": "1.0",
            "type" : "cli_show",
            "chunk" : "0",
            "sid" : "1",
            "input"  : 'show version',
            "output_format" : "json" 
        }
    }

    response = requests.post(url, data=json.dumps(payload),
                            headers=headers, auth=auth)
    print(response)
