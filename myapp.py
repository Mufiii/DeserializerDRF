import requests
import json

URL = "http://127.0.0.1:8000/stucreate/" # endpoint

data = {
  'name': 'Mufees',
  'roll': 127,
  'city':'Calicut'
}
# this data will sent as JSON in post request

json_data = json.dumps(data)
# serializing the data dictionary into a JSON string using json.dumps().

#The program makes a POST request to the specified URL with the JSON data in the request body using the requests.post() method.
response = requests.post(url=URL , data=json_data)
# response from the server is stored in the response variable.

#  response.json() is used to deserialize it into Python data.
data = response.json()
print(data)