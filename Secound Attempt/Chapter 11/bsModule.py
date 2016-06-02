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
    
    #res = requests.get('https://nostarch.com', verify=False)
    res = open('example.html' )
    #try:
        #res.raise_for_status()
    #except Exception as err:
        #print('There was a problem: ' + str(err))
    return(res)

def bsSoup(resobj):
    exampleSoup = bs4.BeautifulSoup(resobj.read(), "html.parser")
    elms = exampleSoup.select('p #author')
    print(type(elms))
    print(len(elms))
    print(elms[0].getText())
    print(elms[0])
    print(elms[0].attrs)
    print

def bsSoup1(resobj):
    exampleSoup = bs4.BeautifulSoup(resobj.read(), "html.parser")
    elms = exampleSoup.select('span')[0]
    print(type(elms))
    print(len(elms))
    print(elms.get('id'))
    print(elms.attrs)

def main():
    resobj=reqPage()
    #bsSoup(resobj)
    bsSoup1(resobj)

if __name__ == '__main__':
    main()