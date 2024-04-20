import json
json_data = '{"var1":"data", "var2":34}'
parsed = json.loads(json_data)
print(parsed)

data2 = {
    'channel_name' : 'QuasarX',
    'cars' : ['bmw', 'audi'],
    'food' : (1,"d")
}

jsonDump = json.dumps(data2)
print(jsonDump)
print(type(jsonDump))