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
    res = requests.get('http://nostarch.com')
    try:
        res.raise_for_status();
    except Exception as exc:
        print('There was a problem: %s' % (exc))
    nostartSoup=bs4.BeautifulSoup(res.text)
    print(nostartSoup)
if __name__ == '__main__':
    main()