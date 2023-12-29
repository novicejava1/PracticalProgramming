#!/usr/bin/env python

f = open('techstack.txt', 'r')
print(f.read())
f.close()

f = open('techstack.txt', 'a')
f.write("InfluxDB Chronograf\n")
f.write("Elastic Stack\n")
f.close()

#f = open('techstack.txt', 'r')
#print(f.read())
#f.close()




