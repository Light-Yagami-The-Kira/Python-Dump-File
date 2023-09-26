import json
json_data = '{"a":1, "b":2, "c":3}'
x = json.loads(json_data)
print(x)
for key in x:
    print(f'{key} ======== {x[key]}')

with open("test.txt", "w") as f:
    json.dump(x,f)