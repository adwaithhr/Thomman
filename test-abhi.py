import requests

url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium"

payload = {
    "enable_google_results": "true",
    "enable_memory": True,
    "input_text": "my dad just died",
    "history_data": [
        {
            "is_sent": True,
            "message": "Respond every query like a professional therapist and separate the answer in points"
        },
    ]
}

# print(payload["history_data"])


headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-KEY": "33d3c098-dd6e-4724-b292-ec01c0a08b73"
}
                    
response = requests.post(url, json=payload, headers=headers)

print(response.text)

payload["history_data"]+=[{
            "is_sent": True,
            "message": payload["input_text"]
        }]

# print(payload["history_data"])