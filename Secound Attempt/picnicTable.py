 #!/usr/bin/python
'''
    File name: picnicTable.py
    Author: ********************
    Date created: 5/12/2016
    Date last modified: 5/12/2016
    Python Version: 3.5.0
'''
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

def main():
    
    picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
    printPicnic(picnicItems, 12, 5)
    printPicnic(picnicItems, 20, 6)

if __name__ == '__main__':
    main()
