"""
This program demonstrates overloading function
Using the __str__ method we can simply print out instances
"""


class Person:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Employee(Person):
    def __init__(self, first, last, staffNum):
        super().__init__(first, last)
        self.staffnumber = staffNum

    # Overriding
    def __str__(self):
        return self.firstname + ' ' + self.lastname + ' ' + str(self.staffnumber)


jane = Person('Jane', 'Doe')
print(jane)

# Overloading
john = Employee('John', 'Doe', 1001)
print(john)
