import math


class Circle:
     # Construct a circle object
     def __init__(self, radius = 1): # note, use two underscore characters
        self.radius = radius # radius is a public variable
     def getPerimeter(self):
        return 2 * self.radius * math.pi
     def getArea(self):
        return self.radius * self.radius * math.pi
     def setRadius(self, radius):
        self.radius = radius

def main():
     # Create a circle1 with radius 1
     circle1 = Circle()
     print("The area of the circle of radius", circle1.radius, "is %.2f" % circle1.getArea())
     # Create a circle with radius 25
     circle2 = Circle(25)
     print("The area of the circle of radius", circle2.radius, "is %.2f" % circle2.getArea())
     # Create a circle3 with radius 125
     circle3 = Circle(125)
     print("The area of the circle of radius", circle3.radius, "is %.2f" % circle3.getArea())
     # Modify circle2 radius
     circle2.radius = 100
     print("The area of the circle of radius", circle2.radius, "is %.2f" % circle2.getArea())
     print("The perimeter of the circle of radius", circle2.radius, "is %.2f" %
    circle2.getPerimeter())

# Start the program
main()