import re

txt = "The rain in Spain"
x = re.search("Spain", txt)
print(x)

if x:
    print("Match found")
else:
    print("No Match found")