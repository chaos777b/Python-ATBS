 #!/usr/bin/python
'''
    File name: commaCode.py
    Author: ********************
    Date created: 5/10/2016
    Date last modified: 5/10/2016
    Python Version: 3.5.0
'''

spam = ['apples', 'bananas', 'tofu', 'cats', 5, '6']

def returnString(listref):
    updateStr =''
    for i in range(int(len(listref) - 1)):
        updateStr =  updateStr + str(listref[i]) +', '

    updateStr = updateStr + 'and ' + str(listref[(int(len(listref)) -1)])

    return updateStr

def main(liststr):
    
    print(returnString(liststr))


if __name__ == '__main__':
    main(spam)
