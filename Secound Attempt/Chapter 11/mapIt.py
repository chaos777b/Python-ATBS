#! python3
'''
    File name: mapIt.py
    Author: ********************
    Date created: 5/27/2016
    Date last modified: 5/27/2016
    Python Version: 3.5.0
'''
import webbrowser, sys, pyperclip


def main():
    if len(sys.argv) >1 :
        address = ' '.join(sys.argv[1:])
        print(address)
    else:
        address = pyperclip.paste()

    webbrowser.open('https://www.google.com/maps/place/' +address)

if __name__ == '__main__':
    main()