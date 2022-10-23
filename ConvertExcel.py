import imp


import csv
import openpyxl

dataFile = 'ExtractFunctions1.csv'

wb = openpyxl.Workbook()
ws = wb.active

with open(dataFile, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        ws.append(row)

wb.save('ExtractFunctions1.xlsx')