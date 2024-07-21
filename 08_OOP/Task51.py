#Create a class with a class attribute a; create an object from it and set ‘a’
#directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:
    a=5

L=Demo()
print(L.a)
L.a=0
print(L.a)
print(Demo.a)
Demo.a=4
print(Demo.a)