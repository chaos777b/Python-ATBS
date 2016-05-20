#! /usr/bin/env python3
'''
    File name: phoneAndEmail.py
    Author: ********************
    Date created: 5/18/2016
    Date last modified: 5/18/2016
    Python Version: 3.5.0
'''
import pyperclip, re

def getClip():
    
    text = str(pyperclip.paste())

    return text

def findPhone(stringData):
    
    phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?              # area code
        (\s|-|\.)?                      # separator
        (\d{3})                         # first 3 digits
        (\s|-|\.)                       # separator
        (\d{4})                         # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
        )''', re.VERBOSE)
    phoneList = phoneRegex.findall(stringData)
    return phoneList


def findEmail(stringData):
    
    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+                # username
        @                               # @ symbol
        [a-zA-Z0-9.-]+                  # domain name
        \.[a-zA-Z]{2,4}               # dot-something
        )''', re.VERBOSE)
    emailList = emailRegex.findall(stringData)
    return emailList

def joinString(phoneData, emailData):
    matches = []
    for groups in phoneData:
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phoneNum += ' x' +groups[8]
        matches.append(phoneNum)
    
    for groups in emailData:
        matches.append(groups)
    return matches


def postClip(string):
    if len(string) > 0:
        pyperclip.copy('\n'.join(string))
        print('Coppied to Clipboard')
        print('\n'.join(string))


def main():

    textString = getClip()
    phoneString = findPhone(textString)
    emailString = findEmail(textString)
    postString = joinString(phoneString, emailString)
    postClip(postString)

if __name__ == '__main__':
    main()

'''
Copied to clipboard:
800-420-7240
415-863-9900
415-863-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
help@nostarch.com
'''