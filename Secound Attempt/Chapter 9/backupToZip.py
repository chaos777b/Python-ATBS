#! /usr/bin/env python3
'''
    File name: backupToZip.py
    Author: ********************
    Date created: 5/12/2016
    Date last modified: 5/12/2016
    Python Version: 3.5.0
'''

import zipfile, os

def findFileName(folder):
    number = 1
    folder = os.path.basename(os.path.abspath(folder))
    while True:
        zipFilename = os.path.basename(folder) + '_'+str(number)+'.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1
    return zipFilename

def createZip(file):
    
    print('Creating %s...' % (file))
    backupZip = zipfile.ZipFile(file, 'w')
    return backupZip

def zipContent(zipFile):
    for foldername, subfolders, filenames in os.walk(os.path.abspath('.')):
        print('Adding files in %s...' % (foldername))
        zipFile.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(os.path.abspath('.')) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            zipFile.write(os.path.join(foldername, filename))
    zipFile.close()
    print('Done.')

def main():
    filename=findFileName('.')
    zipFile = createZip(filename)
    zipContent(zipFile)

if __name__ == '__main__':
    main()