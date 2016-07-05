#! /usr/bin/env python3
'''
    File name: xkcd.py
    Author: ********************
    Date created: 7/04/2016
    Date last modified: 7/04/2016
    Python Version: 3.5.0
'''
import requests, bs4, logging.config, os, json

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

def setup_folder():
    folder ='./xkcd'
    if os.path.isdir(folder) == False:
        try:
            os.mkdir(folder)
        except Exception as err:
            logger.error('There was a problem: ', exc_info=True)
            logger.info('There was a problem: %s' % (err))

def downloadPage(url):
    
    logger = logging.getLogger(__name__) 
    logger.info("Downloading page %s..." % url)
    print('dowloading page %s...' % url)
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as err:
        logger.error('There was a problem: ', exc_info=True)
        logger.info('There was a problem: %s' % (err))
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    return(soup)

def downloadImg(soup)
    comicElem = soup.seelct('#comic img')
    if comicElem == []:
        

def main():
    url = 'http://xkcd.com'
    setup_logging()
    setup_folder()
    logger = logging.getLogger(__name__)  
    logger.info("Starting Program")
    #while not url.endswith('#'):
    soup=downloadPage(url)
    downloadImg(soup)
    #print(soup)

    return  


if __name__ == '__main__':
    
    
    main()


