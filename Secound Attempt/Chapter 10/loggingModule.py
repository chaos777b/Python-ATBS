#! /usr/bin/env python3
'''
    File name: loggingModule.py
    Author: ********************
    Date created: 5/12/2016
    Date last modified: 5/12/2016
    Python Version: 3.5.0
'''
import logging

def main():
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

if __name__ == '__main__':
    main()