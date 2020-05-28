
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


# problem2
class RomanNumber:
    def __init__(self, roman_number):
        self.number = roman_number

    def get_num(self):
        return self.number

    def set_num(self, num1):
        self.number = num1

    def convert_to_num(self):
        num_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for key, value in enumerate(self.number):
            if (key + 1) == len(self.number) or num_dict[value] >= num_dict[self.number[key + 1]]:
                result += num_dict[value]
            else:
                result -= num_dict[value]
        return result

    def convert_to_roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0

        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    # def add(self, x):
    #     return RomanNumber(self.convert_to_roman(self.convert_to_num() + x.convert_to_num()))

    def __add__(self,x):
        return RomanNumber(self.convert_to_roman(self.convert_to_num() + x.convert_to_num()))

    def __sub__(self,x):
        return RomanNumber(self.convert_to_roman(self.convert_to_num() - x.convert_to_num()))

    def __mul__(self,x):
        return RomanNumber(self.convert_to_roman(self.convert_to_num() * x.convert_to_num()))

    def __floordiv__(self,x):
        return RomanNumber(self.convert_to_roman(self.convert_to_num() // x.convert_to_num()))

    def __pow__(self,x):
        return RomanNumber(self.convert_to_roman(self.convert_to_num() ** x.convert_to_num()))

    def check(self):
        assert self.convert_to_roman(self.convert_to_num())==self.get_num(), "Invalid roman number"



a = RomanNumber("IX")
b = RomanNumber("X")
a.check()
b.check()
print(str(a+b))


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




