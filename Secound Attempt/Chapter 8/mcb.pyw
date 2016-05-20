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

def main():
    mcbShelf = openShelve()

    closeShelve(mcbShelf)

if __name__ == '__main__':
    main()
