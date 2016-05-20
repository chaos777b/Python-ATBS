 #!/usr/bin/python3
'''
    File name: magic8Ball2.py
    Author: ********************
    Date created: 5/10/2016
    Date last modified: 5/10/2016
    Python Version: 3.5.0
'''
import random
             
def main():
    messages = ['It is certain',
        'It is decidedly so',
        'Yes definitely',
        'Reply hazy try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook not so good',
        'Very doubtful']

    print(messages[random.randint(0, len(messages) - 1)])

if __name__ == '__main__':
    main()
