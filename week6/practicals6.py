
# problem1
from math import pi
class Circle:
    def __init__(self, color, radius):
        self.color=color
        self.radius=radius
        assert isinstance(self.color,str), "Please input a string"
        assert isinstance(self.radius, (int,float)), "Please input an integer or float"

    def __str__(self):
        return self.color+" circle with radius "+ str(self.radius)

    def area(self):
        return pi*self.radius**2

    def circumference(self):
        return 2*pi*self.radius

    def __add__(self,x):
        return Circle('colored',self.circumference()+x.circumference())

a=Circle('red',2)
b=Circle('blue',1)
print(a+b)

str(a)
print(a)


# problem3
class Person:
    def __init__(self, name, last_name, age, gender, student, password, filename):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.__password = password
        self.filename=filename
        assert isinstance(self.name, str), "Please input a string"
        assert isinstance(self.last_name, str), "Please input a string"
        assert isinstance(self.gender, str), "Please input a string"
        assert isinstance(self.age, int), "Please input an integer"
        assert isinstance(self.filename, str), "Please input a string"

        if isinstance(student, bool):
            self.student = student
        else:
            raise Exception("Student attribute takes values True or False")

    def Greeting(self, second_person):
        return 'Welcome dear {}'.format(second_person.name)

    def Goodbye(self):
        print("Bye everyone!")

    def Favourite_num(self, num1):
        return 'My favorite number is {}'.format(num1)

    def Read_file(self,filename):
        n=self.filename+'.txt'
        try:
            f = open(str(n),"r")
            print(f.read())
        except FileNotFoundError as e:
            print(e)
        except Exception:
            print("Error!")

p1=Person("h","n",4,"female",True,"kkk","filename")
p1.Read_file("filename")




