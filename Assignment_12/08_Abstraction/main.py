'''This program  demonstrates OOP Abstraction'''
from abc import ABC, abstractmethod


class Polygon(ABC):
    def no_of_sides(self):
        pass


# All of the classes below MUST inherit from Polygon class
class Triangle(Polygon):
    def no_of_sides(self):
        print('I have 3 sides')


class Pentagon(Polygon):
    def no_of_sides(self):
        print('I have 5 sides')


class Hexagon(Polygon):
    def no_of_sides(self):
        print('I have 6 sides')


class Quatrilateral(Polygon):
    def no_of_sides(self):
        print('I have 4 sides')


lst = []
lst.append(Triangle())
lst.append(Pentagon())
lst.append(Hexagon())
lst.append(Quatrilateral())


for i in range(0, len(lst)):
    lst[i].no_of_sides()