


def analyzeFuncName(row, colData, wsKeyWords, funcName, funcNameSplit, row_countKeyWords, wsData, hitsArray):
    groupVal = ''
    for row1 in wsKeyWords.iter_cols(min_row = 2, min_col =1, max_col=7, max_row=row_countKeyWords):
        for cell in row1:
            if not (cell.value == None): 
                # print(cell.row, ' ', cell.column)
                # print(cell.value)
                # funcNameSplit = (splitter.split(funcName))
                # funcNameSplit = funcName.split('_')
                # print(funcNameSplit)
                for eachWord in funcNameSplit:
                    if cell.value in eachWord.lower() : #in funcName: #check if keywords are in function name
                        hitsArray.append(funcName + ' ' + wsKeyWords.cell(1, cell.column).value) #if yes, save top level classification
                        groupVal = wsKeyWords.cell(1, cell.column).value
                        if wsData.cell(row,colData+4+ cell.column).value == None:
                            wsData.cell(row,colData+4+ cell.column).value =  1  #increment vote
                        else:
                            wsData.cell(row,colData+4+ cell.column).value = wsData.cell(row,colData+4+ cell.column).value + 1
                        print(funcName + ' ---> ' + groupVal)
                # if not getComments == None :
                #     for eachComment in getComments:
                #         if cell.value in eachComment.lower() : #in funcName: #check if keywords are in function name
                #             print(cell.value + ' ---> ' + eachComment)
                #             if wsData.cell(row,colData+4+ cell.column).value == None:
                #                 wsData.cell(row,colData+4+ cell.column).value =  1  #increment vote
                #             else:
                #                 wsData.cell(row,colData+4+ cell.column).value = wsData.cell(row,colData+4+ cell.column).value + 1

    hitsArrayVal = ' '.join([''.join(sub) for sub in hitsArray])
    wsData.cell(row, colData+3).value = hitsArrayVal
    wsData.cell(row, + colData+4).value = groupVal
    # print(hitsArray)
    hitsArray=[] # re-init array for next function name search 
    groupVal = '' # re-init for next row