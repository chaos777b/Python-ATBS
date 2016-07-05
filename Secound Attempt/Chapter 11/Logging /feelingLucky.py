#! /usr/bin/env python3
'''
    File name: feelingLucky.py
    Author: ********************
    Date created: 6/01/2016
    Date last modified: 6/01/2016
    Python Version: 3.5.0
'''
import requests, sys, webbrowser, bs4, logging.config, os, json

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
    logger.info('Start request to google')
    

    res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
    try:
        res.raise_for_status()
    except Exception as err:
        logger.error('There was a problem: ', exc_info=True)
        logger.info('There was a problem: %s' % (err))


    my_module.foo()
    bar = my_module.Bar()
    bar.bar()

    return  


if __name__ == '__main__':
    
    
    main()