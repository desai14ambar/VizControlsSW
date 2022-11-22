import imp


import csv
import openpyxl

def convert2Excel(dataFile):
    #dataFile = 'ExtractFunctions1.csv'

    wb = openpyxl.Workbook()
    ws = wb.active

    with open(dataFile + '.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            ws.append(row)

    wb.save(dataFile + '.xlsx')
    wb.close()