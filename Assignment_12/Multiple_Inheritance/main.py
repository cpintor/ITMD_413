'''
This program demonstrates Python multiple inheritance
'''

from MyLibrary import *


class Resident(Person, Student):
    def __init__(self, name, age, id):
        # Instantiating Person inside Resident class
        Person.__init__(self, name, age)
        Student.__init__(self, id)


# Start the program
resident7 = Resident('Jane', 33, '1001')
resident7.showName()
resident7.showAge()
print(resident7.getID())
