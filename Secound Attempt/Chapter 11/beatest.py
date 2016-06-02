#! /usr/bin/env python3
'''
    File name: bs4.py
    Author: ********************
    Date created: 5/28/2016
    Date last modified: 5/28/2016
    Python Version: 3.5.0
'''
import requests, bs4

def main():
    res = open('example.html' )
    #try:
        #res.raise_for_status();
    #except Exception as exc:
        #print('There was a problem: %s' % (exc))
    nostartSoup=bs4.BeautifulSoup(res.read(),  "html.parser")
    elems = nostartSoup.select('#author')
    print(len(elems))

if __name__ == '__main__':
    main()