import requests
import json
import os

city = input("Enter City: ")
API = "9234e1f64a484184960171754240702"
BASE_URL = f"http://api.weatherapi.com/v1/current.json?key={API}&q={city}"

r = requests.get(BASE_URL)
a = json.loads(r.text)

# print(a)
# print(a['current'].keys())
print(a['current']['temp_c'])
os.system(f"say {str(a['current']['temp_c'])}")