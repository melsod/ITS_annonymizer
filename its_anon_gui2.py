# GUI builder for .its anonymizer app
# Created by: Sarah MacEwan
# Last Updated: July 11, 2019

# THIS IS A JANKY VERSION THAT REQUIRES THE USER TO KNOW WHAT LINES IN THE ITS FILE THEY WANT ANONYMIZED
# TODO: add buttons for each line in the replacements dict, and then add elim functionality to the create partial file funciton

import sys
import os

if sys.version_info[0] == 2:
    import Tkinter as tk
    import tkFileDialog
    from tkMessageBox import showwarning, askyesno, showinfo, showerror
else:
    import tkinter as tk
    from tkinter import PhotoImage 
    from tkinter import filedialog as tkFileDialog
    from tkinter.messagebox import showwarning, askyesno, showinfo, showerror
    
import webbrowser
import its_anonymizer
import json

#chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %s'


class Anonymizer(object):
    
    def __init__(self, master):
        self.root = master
        self.root.resizable(width=True, height=True)
        self.root.title('ITS Anonymizer')
        self.root.protocol('WM_DELETE_WINDOW')# add function to register pressing the x button as event and call the corresponding function

        program_path = os.getcwd()
        self.frame = tk.Frame(root)
        self.frame.grid(row=0, column=0, sticky='wns', padx=(30, 30), pady=30)
        
        # Instance variables
        self.input_dir = None
        self.output_dir = None
        self.repFile = None # for now, just use the hard-coded replacements dict :)
        self.repFileFullName = 'replacements_dict.json'
        self.repFileFull = open(self.repFileFullName)
        self.repDict = json.load(self.repFileFull)
        
        self.checkbuttonVals = []
        self.primaryChildVar= tk.IntVar()
        self.itsVar= tk.IntVar()
        self.childInfoVar= tk.IntVar()
        self.SRDIVar= tk.IntVar()
        self.childVar = tk.IntVar()
        self.timesVar = tk.IntVar()

        # Menu window
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.submenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Menu', menu=self.submenu)
        #self.submenu.add_command(label = 'run standard anonymization...', command=self.anonymize_its_files_full)
        readme_link = 'https://github.com/BLLManitoba/ITS_anonymizer/blob/master/README.md'
        self.submenu.add_command(label='Help', command=lambda: webbrowser.open_new(readme_link)) # .get(chrome_path).open_new(readme_link))

        # Input/Output Selection Buttons
        self.input_dir_button = tk.Button(
            self.frame,
            text = 'Select input folder', 
            command = self.select_input_its,
            height = 1,
            width = 20,
            relief=tk.GROOVE).grid(row=0, column=1, padx=20, pady=5, sticky='W')

        self.output_dir_button = tk.Button(
            self.frame,
            text = 'Select output folder',
            command = self.select_output_dir,
            height = 1,
            width = 20,
            relief = tk.GROOVE).grid(row = 1, column = 1, padx=20, pady=5, sticky='W')
            
        # Type of info to anonymize checkbuttons
        # I need to decide whether to use the more opaque but easier to use system that Momin made
        # Or if I want to use the 5 main types of info to blur outlined by the non-functional HomeBank code
        # 1. Serial#, 2.Gender, 3. Algorithm age, 4. Child ID, 5. Child Key
        # ALTERNATELY: Child Age, Child Gender, Child ID, Child Key, Recording Datetime
        tk.Label(self.frame, text = "Please select any information you do NOT want anonymized").grid(row=0, column=0, padx=5, pady=5, sticky='NW')
        self.primary_child_checkbox = tk.Checkbutton(
            self.frame,
            text = 'PrimaryChild row',
            variable = self.primaryChildVar).grid(row=1, column = 0, padx=5, pady=5, sticky='NW')
        self.its_checkbox = tk.Checkbutton(
            self.frame,
            text = 'ITS row',
            variable = self.itsVar).grid(row=2, column = 0, padx=5, pady=5, sticky='NW')
        self.child_info_checkbox = tk.Checkbutton(
            self.frame,
            text = 'ChildInfo row',
            variable = self.childInfoVar).grid(row=3, column = 0, padx=5, pady=5, sticky='NW')
        self.srdi_info_checkbox = tk.Checkbutton(
            self.frame,
            text = 'SRDI info row',
            variable = self.SRDIVar).grid(row=4, column = 0, padx=5, pady=5, sticky='NW')
        self.child_checkbox = tk.Checkbutton(
            self.frame,
            text = 'Child row',
            variable = self.childVar).grid(row=5, column = 0, padx=5, pady=5, sticky='NW')
        self.datetime_checkbox = tk.Checkbutton(
            self.frame,
            text = 'Time data rows',
            variable = self.timesVar).grid(row=6, column = 0, padx=5, pady=5, sticky='NW')
            
        # Main (full) anonymizer button
        self.full_anon_button = tk.Button(
            self.frame,
            text = 'Fully anonymize files',
            command = self.anonymize_its_files_full,
            height = 1,
            width = 20,
            relief = tk.GROOVE).grid(row = 2, column = 1, padx=5, pady=5)
        
        # Selective anonymizer button
        self.anon_button = tk.Button(
            self.frame,
            text = 'Partially anonymize files',
            command = self.anonymize_its_files, #throws an error
            height = 1,
            width = 20,
            relief = tk.GROOVE).grid(row = 3, column = 1, padx=5, pady=5)
    
    def get_selection_values(self):
        self.checkbuttonVals = []
        self.checkbuttonVals.append([['PrimaryChild'], self.primaryChildVar.get()])
        self.checkbuttonVals.append([['ITS'], self.itsVar.get()])
        self.checkbuttonVals.append([['ChildInfo'], self.childInfoVar.get()])
        self.checkbuttonVals.append([['SRDInfo'], self.SRDIVar.get()])
        self.checkbuttonVals.append([['Child'], self.childVar.get()])
        self.checkbuttonVals.append([['TransferTime', 'Bar', 'BarSummary', 'Recording', 'FiveMinuteSection', 'Item'], self.timesVar.get()])
        #print self.checkbuttonVals
        return self.checkbuttonVals
    
    def select_input_its(self):
        print('selecting inputs...')
        self.input_dir = tkFileDialog.askdirectory()
        # TODO: pull up a filechooser to select the directory of its files you want anonymized
        # set that directory as your input directory
        
    def select_output_dir(self):
        print('selecting output dir...')
        self.output_dir = tkFileDialog.askdirectory(title='Select where to save your output files')
        # TODO: pull up a filechooser to select where you want to save your anon'd files
        # let them name the directory and then set that as the output dir
        
    def anonymize_its_files_full(self):
        print('input is', self.input_dir)
        print('output is', self.output_dir)
        if self.input_dir == None:
            showwarning('Input folder', 'Please select an input folder')
            return
        elif self.output_dir == None:
            showwarning('Output folder', 'Please select an output folder')
            return
        print("anonymizing your its files the old fashioned way :P")
        its_anonymizer.main(self.input_dir, self.output_dir, self.repFileFullName)
        
    def create_partial_file(self):
        # TODO: add funcionality to select the certain data to anonymize
        # TODO: make it so what is deleted is in accordance with the checkboxes.
        print('making a partial replacements dictionary, based on what was selected...')
        #self.repDict = json.load(self.repFileFull)
        print('initial repDict: ', self.repDict)
        for node in self.repDict.keys():
            #print node
            for item in self.get_selection_values():
                cbVal = item[1]
                for selectName in item[0]:
                    print "item name is: ", selectName
                    if selectName == node:
                        print('cbVal: ', cbVal)
                        if cbVal == 1:
                            print('deleting node: ', node)
                            del self.repDict[node]
           # for name, value in self.repDict[node].items():
            #    print(node)
                #for item in checbuttonVals:
                #    if 
                #elimVal = self.checkbuttonVals[index]
                #if elimval == 1
                #if 
                #    del self.repDict[node]
        with open('partial_replacements_dict.json', 'w') as repf:
            json.dump(self.repDict, repf)
        
    def anonymize_its_files(self):
        print('input is', self.input_dir)
        print('output is', self.output_dir)
        #print('age checkbox vals are: ', self.get_selection_values())
        
        if self.input_dir == None:
            showwarning('Input folder', 'Please select an input folder')
            return
        elif self.output_dir == None:
            showwarning('Output folder', 'Please select an output folder')
            return
        print("anonymizing desired sections of its files...")
        self.create_partial_file()
        its_anonymizer.main(self.input_dir, self.output_dir, 'partial_replacements_dict.json')


if __name__ == '__main__':
    root = tk.Tk()
    x = Anonymizer(root)
    root.mainloop()