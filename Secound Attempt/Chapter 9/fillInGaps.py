#! /usr/bin/env python3
'''
    File name: fillInGaps.py
    Author: ********************
    Date created: 5/23/2016
    Date last modified: 5/23/2016
    Python Version: 3.5.0
'''
import  os, re, shutil

def changeDir(folder):

    os.chdir(folder)
    return

def regPattern():
    
    filePattern = re.compile(r'(.*?)(\d\d\d)(.txt)') # all text before the date
    return filePattern

def searchFiles(filePattern):
    tempList = []
    for fileList in os.listdir():
        mo = filePattern.search(fileList)
        if mo != None:
            tempList.append(fileList)
    return tempList

def renameFiles(filePattern, fileList):
    absWorkingdir = os.path.abspath('.')
    for i in range(len(fileList)-1):
        mo = filePattern.search(fileList[i])
        mo1 = filePattern.search(fileList[i+1])
        if str(mo1.group(2)) == str((int(mo.group(2))+1)):
            continue
        else:
            oldName = os.path.join(absWorkingdir, mo1.group()) 
            newName = os.path.join(absWorkingdir, mo1.group(1) + str(int(mo.group(2))+1) + mo1.group(3))
            shutil.move(oldName, newName) 
            fileList[i+1] = mo1.group(1) + str(int(mo.group(2))+1) + mo1.group(3)
            
   


def main():

    folder = '/Users/jparker/Desktop/test'
    changeDir(folder)
    filePattern=regPattern()
    fielList= searchFiles(filePattern)
    renameFiles(filePattern,fielList)



if __name__ == '__main__':
    main()