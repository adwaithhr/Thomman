import requests

API_ENDPOINT = 'https://api.chatsonic.com/v1/'

API_KEY = '33d3c098-dd6e-4724-b292-ec01c0a08b73'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}',
}

data = {
    'text': 'hello',
    'persona': 'professional',
}

response = requests.post(API_ENDPOINT + 'chat', headers=headers, json=data)

output = response.json()['data'][0]['text']
print(output)