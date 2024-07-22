
'''
Write __str__() method to print the vector as follows:
 7i + 8j +10k 
Assume vector of dimension 3 for this problem.
'''

class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, v2):
        return Vector(self.i + v2.i, self.j + v2.j, self.k + v2.k)
    
    def __mul__(self, v2):
        return Vector(self.i * v2.i, self.j * v2.j, self.k * v2.k)
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

# Test the class with addition and multiplication
v1 = Vector(1, 2, 3)
v2 = Vector(3, 2, 4)

# Test addition
print(v1 + v2)  # Expected output: 4i + 4j + 7k

# Test multiplication
print(v1 * v2)  # Expected output: 3i + 4j + 12k
