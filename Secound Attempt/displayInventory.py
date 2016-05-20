 #!/usr/bin/python
'''
    File name: displayInventory.py
    Author: ********************
    Date created: 5/10/2016
    Date last modified: 5/10/2016
    Python Version: 3.5.0
'''

def displayInventory(inventory):

   
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        item_total = item_total + inventory.get(k, 0)
        print(k + ' ' + str(v))


    print('Total number of Items: ' + str(item_total))

def main():
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    displayInventory(stuff)

if __name__ == '__main__':

    main()