# Write a class “Calculator” capable of finding square, cube and square root of a number.

import math

class Calculator:
    def __init__(self,num):
        self.num=num

    def square(self):
        return self.num*self.num
    
    def cube(self):
        return self.num*self.num*self.num
    
    def squareroot(self):
        return math.sqrt(self.num)
    
    def show(self):
        print(f"The square, cube and sqroot of {self.num} are {self.square()}, {self.cube()} and {self.squareroot()} respectively.")

C1=Calculator(4)
C1.show()
