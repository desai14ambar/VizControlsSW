from openpyxl import load_workbook

dataFile = 'ExtractFunctions1.xlsx'

wb = load_workbook(filename = dataFile)

# grab the active worksheet
ws = wb.active

getCell = ws.cell(row=2, column=1) #633
cellVal = getCell.value
print(cellVal)
stringSplit = cellVal.split('\\')
folderName = stringSplit[0]
stringSplit = stringSplit[1].split('.cpp_')
cppFileName = stringSplit[0]+'.cpp'
funcName = stringSplit[1]
print(cppFileName)
print(funcName)

getCell = ws.cell(row=2, column=2)
cellVal = getCell.value
funcName = (cellVal.partition('\n')[0])
print(funcName)

cppFilePath = folderName + '\\' + cppFileName 

list_of_lines = []
with open(cppFilePath, 'r') as fp:
    for l_no, line in enumerate(fp):
        # search string
        if funcName in line:
            print('string found in a file')
            print('Line Number:', l_no)
            print('Line:', line)
            # don't look for next lines
            list_of_lines.append((l_no, line.rstrip()))
fp.close()
# print(len(list_of_lines))
# print(list_of_lines)
# for elem in list_of_lines:
#         print(elem[0])
t_ype=[]
stopLim = ['}' , ';' , '#']
with open(cppFilePath, 'r') as fp:
    for elem in list_of_lines:
        l_no = elem[0]
        for num in reversed(range(l_no)):
            print(num)
            line = fp.readline(l_no)
            # line = line.rstrip()
            print(line)
            if any(x in line for x in stopLim):
                # print(l_no)
                break
            else:
                # print(l_no)
                t_line = str(line).rstrip('\n')
                t_ype.append(t_line)

print(t_ype)
fp.close()

