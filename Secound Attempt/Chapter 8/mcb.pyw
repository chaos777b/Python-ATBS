#! python3
'''
    File name: mcb.pyw
    Author: ********************
    Date created: 5/20/2016
    Date last modified: 5/20/2016
    Python Version: 3.5.0
'''

import sys, shelve, pyperclip

def openShelve():
    mcbShelf = shelve.open('mcb')
    return mcbShelf

def closeShelve(mcbShelf):
   
   mcbShelf.close()

def checkArgument(mcbShelf):
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':

        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif len(sys.argv) == 2:
        if sys.argv[1].lower() == 'list':
            pyperclip.copy(str(list(mcbShelf.keys())))
        elif sys.argv[1] in mcbShelf:
            pyperclip.copy(mcbShelf[sys.argv[1]])


def main():
    mcbShelf = openShelve()
    checkArgument(mcbShelf)
    closeShelve(mcbShelf)

if __name__ == '__main__':
    main()
