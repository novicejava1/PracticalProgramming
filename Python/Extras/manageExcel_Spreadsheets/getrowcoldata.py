import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']

for rowOfCellObjects in sheet['A1' : 'C3']:
    print(rowOfCellObjects)
    for cellObject in rowOfCellObjects:
        print(cellObject)
        print(cellObject.coordinate, cellObject.value)

