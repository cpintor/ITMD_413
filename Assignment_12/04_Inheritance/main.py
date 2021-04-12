"""
This program demonstrates Inheritance
"""


class Person(object):
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)


# Inheriting from Person class
# This is a child class
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        # Instantiating the superclass constructor
        Person.__init__(self, name, idnumber)

    def display(self):
        print(self.name)
        print(self.idnumber)
        print(self.salary)
        print(self.post)


# start of program
a = Person('Anna', 81178)
a.display()

emp1 = Employee('Anna', 18878, 120000, 'professor')
emp1.display()