import requests
import json

data = {"feature": "test"}

url = "http://127.0.0.1:8888/predict/"

data = json.dumps(data)
response = requests.post(url, data=data)
print(response.json())