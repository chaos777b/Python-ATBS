#! /usr/bin/env python3
'''
    File name: .py
    Author: ********************
    Date created: 5/22/2016
    Date last modified: 5/22/2016
    Python Version: 3.5.0
Say your boss emails you thousands of  les with American-style dates (MM-DD-Y Y Y Y) in their names and needs them renamed to European- style dates (DD-MM-Y Y Y Y). This boring task could take all day to do by hand! Let’s write a program to do it instead.
Here’s what the program does:
• It searches all the  lenames in the current working directory for American-style dates.
• When one is found, it renames the  le with the month and day swapped to make it European-style.
This means the code will need to do the following:
• Create a regex that can identify the text pattern of American-style dates.
• Call os.listdir() to  nd all the  les in the working directory.
• Loop over each  lename, using the regex to check whether it has a date.
• If it has a date, rename the  le with shutil.move().

'''
import shutil, os , re

def regPattern():
    datePattern = re.compile(r'''^(.*?) # all text before the date
        ((0|1)?\d)-                     # one or two digits for the month
        ((0|1|2|3)?\d)-                 # one or two digits for the day
        ((19|20)\d\d)                   # four digits for the year
        (.*?)$                          # all text after the date
        ''', re.VERBOSE)
    return datePattern

def getFiles(regPat):
    euroFilename = []
    amFileName = []
    for amerFileName in os.listdir():
        mo = regPat.search(amerFileName)
        if mo == None:
            continue
        beforePart = mo.group(1)
        monthPart  = mo.group(2)
        dayPart    = mo.group(4)
        yearPart   = mo.group(6)
        afterPart  = mo.group(8)

        euroFilename.append(beforePart + dayPart + '-' + monthPart + '-' 
            + yearPart + afterPart)
        amFileName.append(amerFileName)

    return euroFilename, amFileName

def renameFiles(euFile, amFile):
    absWorkingdir = os.path.abspath('.')
    for i in range(len(euFile)):
        amFile[i] = os.path.join(absWorkingdir, amFile[i])
        euFile[i] = os.path.join(absWorkingdir, euFile[i])
        print('Renaming "%s" to "%s"...' % (amFile[i], euFile[i]))
        shutil.move(amFile[i], euFile[i])

def main():
    regString = regPattern()
    euFile, amFile = getFiles(regString)
    renameFiles(euFile, amFile)

if __name__ == '__main__':
    main()