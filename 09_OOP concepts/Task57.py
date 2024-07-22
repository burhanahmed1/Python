#Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.r} + {self.i}i"

# Test the class with addition and multiplication
c1 = Complex(1, 3)
c2 = Complex(3, 4)

# Test addition
print(c1 + c2)  # Expected output: 4 + 7i

# Test multiplication
print(c1 * c2)  # Expected output: -9 + 13i
