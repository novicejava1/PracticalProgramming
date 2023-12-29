import json

jsondata = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

# Convert JSOn to Python
pythondata = json.loads(jsondata)
print(pythondata)

pythondata = {'name': 'Zophie', 'isCat': True, 'miceCaught': 0, 'felineIQ': None}

# Convert Python to JSON
jsondata = json.dumps(pythondata)
print(jsondata)
