#! /usr/bin/env python3
'''
    File name: regexSearch.py
    Author: ********************
    Date created: 5/21/2016
    Date last modified: 5/12/2016
    Python Version: 3.5.0

Write a program that opens all .txt files in a folder and searches for any
line that matches a user-supplied regular expression. The results should
be printed to the screen.

'''
import os, re, pprint

'''
def getAllFiles():
    files=list(os.listdir())
    return files
'''

'''
def onlyTextFiles(list):
    text = []
    textreg = re.compile(r'\w+.txt$')
    for i in range(len(list)):
        temp=str(textreg.findall(list[i])).strip("[]'")
        #temp=temp.strip("[]'")
        if temp != '':
            text.append(temp)
    return text
'''
def textFiles():
    text = []
    for filename in os.listdir():
        if filename.endswith('.txt'):
            text.append(filename)
    #print(text)
    return text

def searchText(fileList,sstring):
    files = []
    search = re.compile(sstring)

    for i in range(len(fileList)):
        if os.path.isfile(str(fileList[i])) == True:
            file = open(fileList[i], 'r')
            content = file.read()
            if search.findall(content):
                files.append(fileList[i])
        if files =='':
            print('The search did not return any results')

    print('The string you are searching for appears in ')
    pprint.pprint(str(files).strip("[]'"))
        

def searchString():
    print('What do you want to search for')
    string = input()
    return string

def main():

    string=searchString()
    #allfiles=getAllFiles()
    #textFiles=onlyTextFiles(allfiles)
    textList=textFiles()
    searchText(textList,string)

if __name__ == '__main__':
    main()