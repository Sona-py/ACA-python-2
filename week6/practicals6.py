
# problem1
from math import pi
class Circle:
    def __init__(self, color, radius):
        self.color=color
        self.radius=radius
        assert isinstance(self.color,str), "Please input a string"
        assert isinstance(self.radius, int or float), "Please input an integer or float"

    def __str__(self):
        return self.color+" circle with radius "+ str(self.radius)

    def area(self):
        return pi*self.radius**2

    def circumference(self):
        return 2*pi*self.radius

    def __add__(self,x):
        return Circle(self.circumference()+x.circumference())

a=Circle('red',2)
b=Circle('blue',1)
print(a+b)

str(a)
print(a)




