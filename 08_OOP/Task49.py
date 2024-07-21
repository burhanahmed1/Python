#Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    company="Microsoft"

    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def info(self):
        print(f"My name is {self.name}. I am {self.age} years of age. My salary is ${self.salary}")

Burhan=Programmer("Burhan","21","500000")
Burhan.info()

Abdullah=Programmer("Abdullah","12","100000")
Abdullah.info()
