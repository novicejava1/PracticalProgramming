import csv

csvheaderfile = open('scancsvheader.csv')
csvdictReader = csv.DictReader(csvheaderfile)

for row in csvdictReader:
    print(row['Timestamp'],row['Fruit'], row['Quantity'])

