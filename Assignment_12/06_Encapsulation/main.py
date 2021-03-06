'''This program demonstrates Encapsulation within Inheritance'''


class Car (object):
    def __init__(self, make='Ford', model='Explorer', year='2019', milage=0, color='blue'):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__milage = milage
        self.__color = color

    def getModel(self):
        return(self.__model)

    def getColor(self):
        return(self.__color)


# Start of program

# Instance of object class Car
mycar = Car()
print(mycar.getModel())
print(mycar.getColor())