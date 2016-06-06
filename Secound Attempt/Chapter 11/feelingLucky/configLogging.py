#! /usr/bin/env python3
'''
    File name: configLogging.py
    Author: ********************
    Date created: 6/2/2016
    Date last modified: 6/2/2016
    Python Version: 3.5.0
'''

import os
import logging.config
import requests
import sys
import json


def setup_logging(
    default_path='logging.json', 
    default_level=logging.ERROR,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """

    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

def main():
    setup_logging()
    logger = logging.getLogger()
    logger.info('Start reading database')
    res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
    try:
        res.raise_for_status()
    except Exception as err:
        print('There was a problem: ' + str(err))
    return  


    return


if __name__ == '__main__':
    main()
