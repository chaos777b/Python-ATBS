 #!/usr/bin/python3
'''
    File name: allMyCats.py
    Author: ********************
    Date created: 5/10/2016
    Date last modified: 5/10/2016
    Python Version: 3.5.0
'''
def main():

    catNames = []
    while True:
        print('Enter the name of cat ' + str(len(catNames) + 1)
            + ' (Or enter nothing to stop.):')
        name = input()
        if name == '':
            break
        catNames = catNames + [name]  # list concatenation
    print('The cat names are:')

    for name in catNames:
        print('  ' + name)

if __name__ == '__main__':

	main()