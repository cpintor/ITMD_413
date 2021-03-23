"""
This program uses loop to search if a number is in a list
"""

# myList = [10,3,22,15,30,99,11,58,7,44]

# A tuple which cannot be modified
myList = (10,3,22,15,30,99,11,58,7,44)
searchN = eval(input('Enter a number to be searched in a list: '))

for i in range(0, len(myList)):
    if myList[i] == searchN:
        print('Number ', searchN, ' is in the list')

print(myList)
