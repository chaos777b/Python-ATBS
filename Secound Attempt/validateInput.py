 #!/usr/bin/python3
'''
    File name: validateInput.py
    Author: ********************
    Date created: 5/12/2016
    Date last modified: 5/12/2016
    Python Version: 3.5.0
'''

def main():
    while True:
        print('Enter your age:')
        age = input()
        if age.isdecimal():
            break
        print('Please enter a number for your age.')
        
    while True:
        print('Select a new password (letters and numbers only):')
        password = input()
        if password.isalnum():
          break
        print('Passwords can only have letters and numbers.')

if __name__ == '__main__':
    main()
