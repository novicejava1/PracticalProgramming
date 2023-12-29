import csv

outputFile = open('output.csv', 'w', newline='')
outputwriter = csv.writer(outputFile)

outputwriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputwriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputwriter.writerow([1, 2, 3.141592, 4])
outputFile.close()
