#! /usr/bin/env python3
'''
    File name: selectCopy.py
    Author: ********************
    Date created: 5/23/2016
    Date last modified: 5/23/2016
    Python Version: 3.5.0
Write a program that walks through a folder tree and searches for  les with 
a certain  le extension (such as .pdf or .jpg). Copy these  les from whatever 
location they are in to a new folder.
'''
import os, shutil
def changeDir(folder):

    os.chdir(folder)
    foldLocation = os.path.basename(os.getcwd())
    return 

def searchFiles():

    tempfile = []
    for foldername, subfolders, filenames in os.walk(os.getcwd()):
        for files in filenames:
            if files.endswith('.pdf') or files.endswith('.wav'):
                tempfile.append(os.path.join(foldername, files))
    return tempfile

def copyFiles(tempPath, copyPath):
    for i in range(len(tempPath)):
        shutil.copy(tempPath[i], copyPath)


def main():
    folder = '/Users/jparker/Dropbox/Books/Python'
    copyFolder = '/Users/jparker/Desktop/test'
    changeDir(folder)
    tempfile=searchFiles()
    copyFiles(tempfile, copyFolder)

if __name__ == '__main__':
    main()