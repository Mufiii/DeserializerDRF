import requests
import json

URL = "http://127.0.0.1:8000/stucreate"

data = {
  'name': 'Mufees',
  'roll': 127,
  'city':'Calicut'
}

json_data = json.dumps(data)

response = requests.post(url=URL , data=json_data)
data = response.json()
print(data)