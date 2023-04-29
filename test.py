import requests
import json

API_ENDPOINT = 'https://api.writesonic.com/v1/'

API_KEY = '33d3c098-dd6e-4724-b292-ec01c0a08b73'

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-KEY": "33d3c098-dd6e-4724-b292-ec01c0a08b73"
}

data = {
    'text': 'hello there',
    'model': 'general',
    'num_results': 1,
    'max_length': 1024,
}

response = requests.post(API_ENDPOINT + 'auto-gpt-3',
                         headers=headers, data=json.dumps(data))

output = response
print(output)
