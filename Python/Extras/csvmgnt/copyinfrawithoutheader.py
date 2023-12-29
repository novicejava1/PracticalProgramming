import csv

csvfile = open('infrawithheader.csv')
csvheaderreader = csv.DictReader(csvfile)

outputFile = open('infrawithoutheader.csv', 'w', newline='' )
csvwriter = csv.writer(outputFile)

for row in csvheaderreader:
    print(row['Environment'], row['Server'], row['Replicas'])
    csvwriter.writerow([row['Environment'], row['Server'], row['Replicas']])

csvfile.close()
outputFile.close()


