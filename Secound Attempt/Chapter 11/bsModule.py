#! /usr/bin/env python3
'''
    File name: bsModule.py
    Author: ********************
    Date created: 6/1/2016
    Date last modified: 6/1/2016
    Python Version: 3.5.0
'''
import requests, bs4

def reqPage():
    
    res = requests.get('https://www.nostarch.com')
    try:
        res.raise_for_status()
    except Exception as err:
        print('There was a problem: ' + str(err))
    print(type(res))
    return(res)

def bsSoup(resobj):
    exampleSoup = bs4.BeautifulSoup(resobj.text, "html.parser")
    elms = exampleSoup.select('p #author')
    print(type(elms))
    print(len(elms))

def main():
    resobj=reqPage()
    bsSoup(resobj)

if __name__ == '__main__':
    main()