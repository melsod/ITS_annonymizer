# ITS file anonymizer

DISCLAIMER: Please read this readme carefully so that you ensure you understand what data are being anonymized, and what data are being left in their original format.

This version of the its anonymizer processes files line-by-line via a text editor, preserveing the original structure of the its file.
It allows the user to choose the folder that contains the original its files, and to choose the folder where they would like to save their anonymized files.

## To use

1. Double click on the file 'its_anon_gui2.py' This will launch a user interface with several buttons
2. Select input folder (allows user to choose input .its files)
3. Select output folder (allows user to choose where to save anonymized files - it is recommended to have an empty output folder already made!)
4. Fully anonymize files (anonymizes all the sensitive/non-anonymous data in the files)
5. Partially anonymize files (anonymizes only data specified)
6. checkbuttons: when selected, the data in that row of the .its file will be left in its original format

## Changes

    Dates:		1000-01-01 00:00:00 (January 1, 1000, 12 AM)
    Time zone: 	AAA
    Gender: 	A
    Child key: 	9A99AAA999999A99

This information is stored in `replacement_dict.json` will dictate what the anonymized file will have. This file can be modified to include other information that needs to be private.

If timestamps needs to be kept as it its the format will be the following:

	"startClockTime": [{"replace_value":"1000-01-01"},{"only_time":"true"}]

This will only replace the date and keep the timestamp for further analysis.

## Checkbuttons

Each checkbutton, if checked will exclude the corresponding row of data from anonymization. Data in each row are:

1. PrimaryChild row: date of birth, gender, child key
2. ITS row: file name, time file was created
3. ChildInfo row: date of birht, gender
4. SRDInfo row: serial number
5. Child row: date of birth, gender, enrollment date, child ID, child key
6. Time data rows: all instances of timestamps throughout the file (if "only_time" is set to true, the timestamps, but not dates, will be preserved)