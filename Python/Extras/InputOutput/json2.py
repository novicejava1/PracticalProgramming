import json

x = [1, 'simple', 'list']

f = open("json.txt", "w")
json.dump(x, f)
f.close()

f = open("json.txt", "r")
x = json.load(f)
print(x)
f.close()
