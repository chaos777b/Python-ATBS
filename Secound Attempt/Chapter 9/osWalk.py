#! /usr/bin/env python3
'''
    File name: .py
    Author: ********************
    Date created: 5/12/2016
    Date last modified: 5/12/2016
    Python Version: 3.5.0
'''
import os

def main():
 
    print("root prints out directories only from what you specified")
    print("dirs prints out sub-directories from root")
    print ("files prints out all files from root and directories")
    print( "*" * 20)
    for root, dirs, files in os.walk("/var/log"):
        print(root)
        print(dirs)
        print(files)
if __name__ == '__main__':
    main()