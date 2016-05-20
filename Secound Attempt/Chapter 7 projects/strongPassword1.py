#! /usr/bin/env python3
'''
    File name: strongPassword.py
    Author:********************
    Date created: 5/18/2016
    Date last modified: 5/18/2016
    Python Version: 3.5.0

Strong Password Detection
    Write a function that uses regular expressions to make sure the password 
    string it is passed is strong. A strong password is defined as one that is
    at least eight characters long, contains both uppercase and lowercase
    characters, and has at least one digit. You may need to test the string 
    against multiple regex patterns to validate its strength
'''
import pyperclip, re

def getClip():
    
    text = str(pyperclip.paste())

    return text

def testStrength(testString):

    rregex = re.compile(r'[a-z]+|[A-Z]+|\d+')
    testReg = rregex.findall(testString)

    print(testReg)
    #if len(testReg) == 3 and len(testString) >= 8:
        #return True
    #else:
        #return False

def main():

    textString = getClip()
    if testStrength(textString) == True:
        print('This is a string password.')
    else:
        print('This is not a strong password.')

if __name__ == '__main__':
    main()

'''
IKS1G!RIeEAT99
'''