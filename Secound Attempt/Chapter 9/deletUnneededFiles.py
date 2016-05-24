#! /usr/bin/env python3
'''
    File name: deletUnneededFiles.py
    Author: ********************
    Date created: 5/12/2016
    Date last modified: 5/12/2016
    Python Version: 3.5.0
Deleting Unneeded Files
It’s not uncommon for a few unneeded but humongous  les or folders to take up 
the bulk of the space on your hard drive. If you’re trying to free up
room on your computer, you’ll get the most bang for your buck by deleting the 
most massive of the unwanted  les. But  rst you have to  nd them.
Write a program that walks through a folder tree and searches for excep- 
tionally large  les or folders—say, ones that have a  le size of more than 
2MB. (Remember, to get a file’s size, you can use os.path.getsize() from the 
os module.) Print these files with their absolute path to the screen.
'''

import os 
def changeDir(folder):

    os.chdir(folder)
    foldLocation = os.path.basename(os.getcwd())
    return 

def searchFiles():

    tempfile = []
    for foldername, subfolders, filenames in os.walk(os.getcwd()):
        for files in filenames:
            if (round(os.path.getsize(files) / 1024**2,  2)) >=2:
                tempfile.append(os.path.join(foldername, files))
    return tempfile 

def delFiles(tempPath):
    for i in range(len(tempPath)):
        print(tempPath[i])


def main():
    folder = '/Users/jparker/Desktop/Screen Shots'
    changeDir(folder)
    tempfile = searchFiles()
    delFiles(tempfile)

if __name__ == '__main__':
    main()