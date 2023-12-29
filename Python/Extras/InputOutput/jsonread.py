import json

f = open("json.txt", "r")
data = json.load(f)
print(data)
f.close()


f2 = open("test.json", "w")
soapdata = ["test", "it", "fully"]
json.dump(soapdata, f2)
f2.close()

f2 = open("test.json")
print(json.load(f2))
f2.close()
