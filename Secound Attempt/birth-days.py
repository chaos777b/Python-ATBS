 #!/usr/bin/python
'''
    File name: birth-days.py
    Author: ********************
    Date created: 5/10/2016
    Date last modified: 5/10/2016
    Python Version: 3.5.0
'''

def main():
    birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
    while True:
        print('Enter a name: (blank to quit)')
        name = input()
        if name == '':
            break
        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
        else:
            print('I do not have birthday information for ' + name)
            print('What is their birthday?')
            bday = input()
            birthdays[name] = bday
            print('Birthday database updated.')

if __name__ == '__main__':
    main()