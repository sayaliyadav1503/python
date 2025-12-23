import json

json_str = '{"name": "Amit", "age": 22}'
data = json.loads(json_str)

print(data)
print(type(data))
