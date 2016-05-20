#! /usr/bin/env python3
'''
    File name: bulletPointAdder.py
    Author: ********************
    Date created: 5/12/2016
    Date last modified: 5/12/2016
    Python Version: 3.5.0
'''
import pyperclip

def seperateText(text):
    lines = text.split('\n')
    for i in range(len(lines)):
        strip = lines[i]
        strip = strip.lstrip('#')
        lines[i] = '* ' + strip
    return lines

def joinText(sepTxt):
        
    joinTxt = '\n'.join(sepTxt)

    return joinTxt

def main():
    
    text = pyperclip.paste()
    testList=seperateText(text)
    text = joinText(testList)
    
    for i in range(len(testList)):
        print(testList[i])

    pyperclip.copy(text)
    

if __name__ == '__main__':
    main()

#Lists of animals
#Lists of aquarium life
#Lists of biologists by author abbreviation
#Lists of cultivars