import requests
import json

url = "https://petstore.swagger.io/v2/store/order/3"

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers)

assert response.status_code == 200

print(response.text)