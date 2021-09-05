import requests
import json

url = "https://petstore.swagger.io/v2/store/order"

payload = json.dumps ({
  "id": 3,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2021-09-05T09:48:36.698Z",
  "status": "placed",
  "complete": "true"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

assert response.status_code == 200

print(response.text)