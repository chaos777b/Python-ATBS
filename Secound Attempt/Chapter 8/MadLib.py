#! /usr/bin/env python3
'''
    File name: MadLib.py
    Author: ********************
    Date created: 5/21/2016
    Date last modified: 5/21/2016
    Python Version: 3.5.0

Create a Mad Libs program that reads in text files and lets the user add
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file. For example, a text file may look like this:

The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
Enter an adjective:

silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
'''
import os, re

def getFile():

    if os.path.isfile('madlib.txt') == True:
        file=open ('madlib.txt', 'r')
        contents = file.read()
        file.close()
    return(contents)

def getUserinput():

    userInput=[]
    print('Enter an adjective:')
    item= input()
    userInput.append(item) 
    print('Enter a noun:')
    item= input()
    userInput.append(item) 
    print('Enter a verb:')
    item= input()
    userInput.append(item) 
    print('Enter a noun:')
    item= input()
    userInput.append(item) 
    print(userInput)
    return(userInput)

def replaceText(content, text):
    madList = ['ADJECTIVE','NOUN','VERB','NOUN']
    for i in range(4):
        replace = re.compile(madList[i])
        content=replace.sub(text[i], content, 1)
    return(content)

def writeContent(fileText):
    file=open ('madlib.txt', 'w')
    file.write(fileText)
    print(fileText)
    closefile(file)

def closefile(file):

    file.close()

def main():

    fileContents = getFile()
    inputText=getUserinput()
    fileContents = replaceText(fileContents, inputText)
    writeContent(fileContents)

if __name__ == '__main__':
    main()