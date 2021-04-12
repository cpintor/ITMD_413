import math

class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def getPerimeter(self):
        return (2 * self.radius * math.pi)

    def getArea(self):
        return self.radius * self.radius * math.pi

    def setRadius(self, radius):
        self.radius = radius


# Start of the program
circle1 = Circle()
print("The area of the circle of radius", circle1.radius, "is %.2f" % circle1.getArea())
print('The perimeter is %.2f' % circle1.getPerimeter())

circle1 = Circle(125)
print("The area of the circle of radius", circle1.radius, "is %.2f" % circle1.getArea())
print('The perimeter is %.2f' % circle1.getPerimeter())

circle1.setRadius(125)
print("The area of the circle of radius", circle1.radius, "is %.2f" % circle1.getArea())
print('The perimeter is %.2f' % circle1.getPerimeter())