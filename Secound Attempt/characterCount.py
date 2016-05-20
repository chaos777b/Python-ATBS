 #!/usr/bin/python
'''
    File name: characterCount.py
    Author: ********************
    Date created: 5/10/2016
    Date last modified: 5/10/2016
    Python Version: 3.5.0
'''
import pprint

def main():
    
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    count = {}
    
    for character in message.lower():
        count.setdefault(character, 0)
        count[character] = count[character] + 1
    pprint.pprint(count)


if __name__ == '__main__':
    main()