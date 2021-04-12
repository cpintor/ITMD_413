"""
Python functions getters and setters
getters are also called Accessor functions
setters are also called Mutator functions
"""


class Employee:
    # Constructor
    def __init__(self, first, last):
        self.__first = first
        self.__last = last

    def getFirst(self):
        return (self.__first)

    def getLast(self):
        return (self.__last)

    def setFirst(self, first):
        self.__first = first


emp1 = Employee('Jane', 'Doe')
print('The first name is', emp1.getFirst())
print('The last name is', emp1.getLast())

# Resetting value of first name
emp1.setFirst('John')
print('The first name is', emp1.getFirst())
