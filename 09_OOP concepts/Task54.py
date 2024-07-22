# Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class Vector_2D:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class Vector_3D(Vector_2D):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k=k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a=Vector_2D(1,2)
b=Vector_3D(3,4,5)

a.show()
b.show()


