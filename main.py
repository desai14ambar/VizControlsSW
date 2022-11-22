from pickle import FALSE
from ExtractComments import getComments
from openpyxl import load_workbook
from functiondefextractor import core_extractor
from ConvertExcel import convert2Excel

srcPath = r'Arducopter'
dataFile = 'ExtractFunctions'
genDataFile = FALSE

if genDataFile:
    output0 = core_extractor.extractor (srcPath, exclude=r'*.h, *.txt, wscript, Makefile.waf')
    output0.to_csv(dataFile +'.csv')  # local folder file , adds sr no #

    convert2Excel(dataFile)

dataFile = dataFile + '.xlsx'

wb = load_workbook(filename = dataFile)

# grab the active worksheet
ws = wb.active
row_count = ws.max_row

column = 2
for row in range(2, row_count):
    print(row)
    getComments(row, column, ws)

wb.save(filename = dataFile)
wb.close()