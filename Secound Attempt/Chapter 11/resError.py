#! /usr/bin/env python3
'''
    File name: resError.py
    Author: ********************
    Date created: 5/28/2016
    Date last modified: 5/28/2016
    Python Version: 3.5.0
'''
import requests

def main():
    res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))
    playFile = open('RomeAndJuliet.txt', 'wb')
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
    playFile.close 

if __name__ == '__main__':
    main()