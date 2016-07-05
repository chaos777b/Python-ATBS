#! /usr/bin/env python3
'''
    File name: xkcd.py
    Author: ********************
    Date created: 7/04/2016
    Date last modified: 7/04/2016
    Python Version: 3.5.0
'''
import requests, webbrowser, bs4, logging.config, os, json

def setup_logging(
    default_path='logging.json', 
    default_level=logging.INFO,
    env_key='LOG_CFG'):
    
    """
    Setup logging configuration
    """

    path = default_path
    value = os.getenv(env_key, None)
    logpath ="./logs"

    logging.info('Verifying Log Fodler is created.')

    if os.path.isdir(logpath) == False:
            os.mkdir(logpath)
       
        

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
    logger = logging.getLogger(__name__)  

    return  


if __name__ == '__main__':
    
    
    main()


