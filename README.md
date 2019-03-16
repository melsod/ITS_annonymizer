# ITS file anonymizer
This version of the its anonymizer processes files with a simple text editor, which allows to preserve original structure of the its file. It takes a path of the folder that contains the original its files (input its) and creates a copy of that folder with anonymized files  named 'inputfolder_anonymised' on the same file location.

##To use

1. Open the command window and navigate to the program folder. Or open the program folder, Shift+right-click on empty space, 'Open command window here'
2. Copy path of the folder with the its files (change drive if necessary, i.e., `S:`)
3. In the command winodw type `python its_anonymizer.py` and paste the path which contains the input its files. Command should look like this:
`python its_anonymizer.py "C:\input_its_folder`

The program will create a new folder in the same directory as the input folder adding suffix "_anonymized". If it exists, it will NOT override; throw an exception. 

##Changes

    Dates:		1000-01-01 00:00:00 (January 1, 1000, 12 AM)
    Time zone: 	AAA
    Gender: 	A
    Child key: 	9A99AAA999999A99

This information is stored in `replacement_dict.json` will dictate what the anonymized file will have. This file can be modified to include other information that needs to be private.