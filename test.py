# test_request.py
import requests

url = "http://localhost:8000/"
data = {
    "name": "Sample Item",
    "description": "This is a description of the sample item.",
    "price":10
}

response = requests.post(url, json=data)
print(response.json())