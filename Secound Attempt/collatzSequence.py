 #!/usr/bin/python
'''

    File name: collatzSequence.py
    Author: ********************
    Date created: 5/10/2016
    Date last modified: 5/11/2016
    Python Version: 3.5.0

'''
def collatz(numItn):
    if numItn % 2 ==0:
        numItn= numItn //2
        print(str(numItn))
    else:
        numItn = 3* numItn +1
        print(str(numItn))

    return(numItn)

def inputValidtion(testNum):

    while True:
        try:
            valid=int(testNum)
            return valid
            break
        except ValueError:
            print('Error, you did not enter a  valid number!')
            print('Please enter a valid number:', end='')
            testNum=input()


def main():
    print('Please enter a number:', end='')
    testinput=input()
    validInt=inputValidtion(testinput)

    while validInt !=1:
        validInt= collatz(validInt)


if __name__ == '__main__':
    main()
