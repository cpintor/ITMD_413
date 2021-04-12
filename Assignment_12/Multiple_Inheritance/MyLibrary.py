class Person:
    def __init__(self, personName, personAge):
        self.name = personName
        self.age = personAge

    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)


class Student:
    def __init__(self, studentID):
        self.studentID = studentID

    def getID(self):
        return (self.studentID)