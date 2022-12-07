
from ExtractComments import getComments
from openpyxl import load_workbook
from ConvertExcel import convert2Excel, createDataFile
from analyzeDataFile import analyzeData
from finalVote import finalVotefcn
from vizDataEx import createViz

from GUIfactory import *
from  tkinter import filedialog
import os

from instruct1 import instructs

# srcPath = r'Arducopter'
dataFile = 'VizControlsSWDatabase'
genDataFile = TRUE

swPath = ''

master = Tk()

master.title("VizControlsSW CIS 580 Fall 2022 - by Ambar Desai ")
master.geometry("1600x1200")

title = Label(master, text= "Project Folder")
# title.grid(row=0, column = 0, sticky=W, pady=2)
title.place(x=10, y=10)

def getPath():
    cwd = os.getcwd()
    global swPath
    swPath = filedialog.askdirectory(initialdir=cwd)
    swPath = swPath.split('/')
    swPath = (swPath[len(swPath)-1])
    print(swPath)
    return swPath

searchPath = GUIFactory(ButtonFactory).create(master, "Path", 0, 1, "W", getPath) #create main search button
# searchPath.label_obj.configure(command = getPath())
# searchPath.label_obj.grid(padx = 10, pady = 10)
searchPath.label_obj.place(x = 100, y = 10)

genDatabase = GUIFactory(ButtonFactory).create(master, "Generate Database", 1, 1, "W", lambda: createDataFile(swPath, genDataFile, dataFile)) #create main search button
# genDatabase.label_obj.grid(padx = 10, pady = 10)
genDatabase.label_obj.place(x = 50, y = 50)

def getExcelFile():
    cwd = os.getcwd()
    filePath = filedialog.askopenfilename(initialdir=cwd, filetypes=[("Excel files", ".xlsx")])
    filePath = filePath.split('/')
    filePath = (filePath[len(filePath)-1])
    return filePath

def getDataFile():
    filePath = getExcelFile()
    analyzeData(filePath)
    finalVotefcn(filePath)
    print(filePath)

genDatabase = GUIFactory(ButtonFactory).create(master, "Analyze", 2, 1, "W", getDataFile) #create main search button
#searchPath.label_obj.configure(command = getPath)
genDatabase.label_obj.place(x=180, y = 50)

def vizDataFile(win):
    filePath = getExcelFile()
    createViz(win,filePath)

vizDatabase = GUIFactory(ButtonFactory).create(master, "Visualize", 2, 1, "W", lambda: vizDataFile(master)) #create main search buttonVisualize
vizDatabase.label_obj.place(x=250, y = 50)

instructs2 = Label(master, text= instructs, justify=LEFT)
instructs2.place(x=330, y=10)

mainloop()



