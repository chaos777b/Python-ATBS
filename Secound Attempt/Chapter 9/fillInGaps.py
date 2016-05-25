#! /usr/bin/env python3
'''
    File name: fillInGaps.py
    Author: ********************
    Date created: 5/23/2016
    Date last modified: 5/23/2016
    Python Version: 3.5.0
'''
import os

def changeDir(folder):

    os.chdir(folder)
    foldLocation = os.path.basename(os.getcwd())
    return

def regPattern():
    
    filePattern = re.compile(r'.*?\d\d\d.txt') # all text before the date
    return filePattern

def searchFiles():
    
def main():

    folder = '/Users/jparker/Desktop/test'
    changeDir(folder)
    filePattern=regPattern()

if __name__ == '__main__':
    main()