class Person:
    def __init__(self, name, last_name, age, gender, student, password):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.student = bool(student)
        self.__password = password

    def Greeting(self, name):
        print("Welcome dear", name)

    def Goodbye(self):
        print("Bye everyone!")

    def Favourite_num(self, num1):
        print("My favorite number is", num1)

Person1=Person("Sona","Kirakosyan",27,"female", True, "freedom")

Person.Greeting(Person1,"Sona")

