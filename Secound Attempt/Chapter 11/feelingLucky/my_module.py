#! /usr/bin/env python3
'''
    File name: my_module.py
    Author: ********************
    Date created: 6/2/2016
    Date last modified: 6/2/2016
    Python Version: 3.5.0
'''

import logging, requests



def foo():
    logger = logging.getLogger(__name__)
    logger.info('Hi, foo')
class Bar(object):

    def __init__(self, logger=None):
        self.logger = logger or logging.getLogger(__name__)

    def bar(self):
        self.logger.info('Hi, bar')
        res = requests.get('http://apple.com')
        self.logger.error('test error')
        self.logger.warn('test warn')
def main():

    return 

if __name__ == '__main__':
    main()