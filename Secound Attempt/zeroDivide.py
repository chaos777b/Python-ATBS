 #!/usr/bin/python3
'''
    File name: zeroDivide.py
    Author: ********************
    Date created: 5/10/2016
    Date last modified: 5/10/2016
    Python Version: 3.5.0
'''
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError: 
        print('Error: invalid argument')

def main():
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))

if __name__ == '__main__':
    main()
