import requests
import json

url = "https://petstore.swagger.io/v2/store/order/3"

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers)

assert response.status_code == 200, "Order not found"

print(response.text)