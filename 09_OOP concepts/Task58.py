# Write a class vector representing a vector of n dimensions. Overload the + and *  operator which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __add__(self, v2):
        return Vector(self.i + v2.i, self.j + v2.j, self.k + v2.k)
    
    def __mul__(self, v2):
        return Vector(self.i * v2.i, self.j * v2.j, self.k * v2.k)
    
    def __str__(self):
        return f"Vector({self.i}, {self.j}, {self.k})"


v1=Vector(1,2,3)
v2=Vector(3,2,4)

print(v1 + v2)
print(v1 * v2)