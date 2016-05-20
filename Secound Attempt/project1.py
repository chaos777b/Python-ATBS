#! /usr/bin/env python3
'''
    File name: .py
    Author: ********************
    Date created: 5/12/2016
    Date last modified: 5/12/2016
    Python Version: 3.5.0
'''
import sys, pyperclip

def copyPassword(account, passdict):
    if account in passdict:
        pyperclip.copy(passdict[account])
        print('Password for ' + account + ' coppied to the clipboard.')
    else:
        print('Thre is no account named ' + account)

def checkArgv():
 
    if len(sys.argv) < 2:
        print('Usage: python3 pw.py [account] - copy account password')
        sys.exit()
    return sys.argv[1]

def main():
    PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

   
    account=checkArgv()
    copyPassword(account, PASSWORDS)
    
if __name__ == '__main__':
    main()
