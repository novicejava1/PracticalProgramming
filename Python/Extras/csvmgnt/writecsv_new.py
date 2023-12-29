import csv

outputFile = open('output_new.csv', 'w', newline='')
outputwriter = csv.writer(outputFile, delimiter='\t', lineterminator='\n\n')

outputwriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputwriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputwriter.writerow([1, 2, 3.141592, 4])
outputFile.close()
