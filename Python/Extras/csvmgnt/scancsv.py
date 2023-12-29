import csv

csvfile = open('example.csv')
csvreader = csv.reader(csvfile)

# Convert csv data to list
#csvdata = list(csvreader)
#print(csvdata)

# Extract a particular row and col data
#print(csvdata[0][1])

# Extract all the fruits
#for data in csvdata:
#    print(data[1])

# Extract all the rows data
for row in csvreader:
    print(str(row))
    print('Row #' + str(csvreader.line_num) + ' ' + str(row))

