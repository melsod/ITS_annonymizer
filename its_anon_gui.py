# GUI builder for .its anonymizer app
# Created by: Sarah MacEwan
# Last Updated: July 9, 2019

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
import its_anonymizer as anoner


class Anonymizer(object):
    
    def __init__(self, master):
        self.root = master
        self.root.resizable(width=False, height=False)
        self.root.title('ITS Anonymizer')
        self.root.protocol('WM_DELETE_WINDOW')# add function to register pressing the x button as event and call the corresponding function

        program_path = os.getcwd()
        self.frame = tk.Frame(root)
        self.frame.grid(row=0, column=0, sticky='wns', padx=(30, 30), pady=30)

        # Menu window
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.submenu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Menu', menu=self.submenu)
        self.submenu.add_command(label = 'run standard anonymization...')
        readme_link = 'https://github.com/BLLManitoba/ITS_anonymizer/blob/master/README.md'
        self.submenu.add_command(label='Help', command=lambda: webbrowser.open_new(readme_link))

        w = tk.Label(root, text = "Hello, world!").grid(row = 0, column = 0)
        # TODO:
            # Add buttons to select directory of its files
            # Add a set of checkboxes to list off the things that they want anonymized
            # Add a "save anonymized files as..." button so they can save the files in a specified location
            # Add a big old "anonymize" button :D

    def anonymize_its_files(self):
        print("anonymizing your its files the old fashioned way :P")
        self.its_anonymizer.main()


if __name__ == '__main__':
    root = tk.Tk()
    x = Anonymizer(root)
    root.mainloop()