 #!/usr/bin/python
'''
    File name: allguests.py
    Author: ********************
    Date created: 5/10/2016
    Date last modified: 5/10/2016
    Python Version: 3.5.0
'''

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

def main():
    allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
        'Bob': {'ham sandwiches': 3, 'apples': 2},
        'Carol': {'cups': 3, 'apple pies': 1}}

    print('Number of things being brought:')
    print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
    print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
    print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
    print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
    print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))

if __name__ == '__main__':

    main()