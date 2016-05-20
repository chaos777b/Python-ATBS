#! /usr/bin/env python3
'''
    File name: tablePrinter.py
    Author: ********************
    Date created: 5/12/2016
    Date last modified: 5/12/2016
    Python Version: 3.5.0
'''
def longTable(table):

    colWidths = [0] * len(table)

    for i in range(len(table)):
        for y in range(len(table[i])):
            #print('Table '+ str(table[i][y]))
            if int(colWidths[i]) <  len(table[i][y]):
                colWidths[i] = len(table[i][y])        
    return colWidths 

def printTable(Width, Data):
    i=0
    for y in range(len(Data[i])):
        print('\n', end='')
        for i in range(len(Data)):
            print(str(Data[i][y]).rjust(Width[i]) + '   ',  end='')
    print('')



def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                ['Alice', 'Bob', 'Carol', 'David'],
                ['dogs', 'cats', 'moose', 'goose']]
    listWidth = longTable(tableData)

    printTable(listWidth, tableData)

if __name__ == '__main__':

    main()