# Python Code for factory method
# it comes under the creational
# Design Pattern
from tkinter import *

class gui_object(object):
    def create_object():
        pass


class LabelFactory(gui_object):
    label_obj = ""
    
    def create_object(self, master1,text1,row1,column1,sticky1,pady1):
        self.label_obj = Label(master1, text = text1)
        self.label_obj.grid(row = row1, column = column1, sticky = sticky1, pady = pady1)
        return self

class ButtonFactory(gui_object):
    label_obj = ""
    
    def create_object(self, master1,text1,row1,column1,sticky1, fcn):
        self.label_obj = Button(master1, text = text1, command= fcn)
        self.label_obj.grid(row = row1, column = column1, sticky = sticky1)
        return self

    def getSearch(self):
        s ="search"
        #print("search")


class CheckFactory(gui_object):
    label_obj = ""
    
    def create_object(self, master1,text1,checkvar,row1,column1,sticky1):
        self.label_obj = Checkbutton(master1, text = text1, variable=checkvar, onvalue=True, offvalue=False)
        self.label_obj.grid(row = row1, column = column1, sticky = sticky1, columnspan = 2)
        return self

class ListOptionsFactory(gui_object):
    label_obj = ""
    listObj = ""
    choice = ""
    ListChange = ""

    def create_object(self, master1, ListHandle, ListOptions, row1, column1, pady1):
        self.listObj = ListOptions
        self.ListChange = ListHandle
        #self.label_obj = OptionMenu(master1, ListHandle, *self.listObj)
        """ def option_changed(*args): #return value on change
            self.choice = self.ListChange.get()
            #print(choice)
            return self.choice """
        self.label_obj = OptionMenu(master1, ListHandle, *self.listObj, command=self.option_changed)
        self.label_obj.grid(row = row1, column = column1, pady = pady1)
        self.choice = StringVar()
        return self

    def option_changed(self, ListHandle, *args): #return value on change
        self.choice = self.ListChange.get()
        ListHandle = self.choice
        #print(self.choice)
        return ListHandle


class GUIFactory:
    choice = ""
    def __init__(self, factory):
        #return factory()
        self.create = factory().create_object  #()#master1,text1,row1,column1,sticky1,pady1)