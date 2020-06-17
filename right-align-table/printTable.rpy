#! python3
# printTable.py - Prints the table's values aligned to the right side
import sys

tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]


def printTable(table: list) -> None:
    if len(table) == 0:
        print('Please provide the table with values')
        sys.exit()
    for row in table:
        for col in row:
            print(str(col), end=" ")
        print('')


printTable(table=tableData)
