import requests
import json

url = "https://petstore.swagger.io/v2/store/inventory"

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers)

assert response.status_code == 200

print(response.text)