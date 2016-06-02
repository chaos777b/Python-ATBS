#! /usr/bin/env python3
'''
    File name: feelingLucky.py
    Author: ********************
    Date created: 6/01/2016
    Date last modified: 6/01/2016
    Python Version: 3.5.0
'''
import requests, sys, webbrowser, bs4

def main():
    print('Googleing...')
    res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
    try:
        res.raise_for_status()
    except Exception as err:
        print('There was a problem: ' + str(err))
    
if __name__ == '__main__':
    main()