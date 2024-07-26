#  Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

def find_max(a,b):
    if(a>b):
        return a
    else:
        return b

l=[1,2,3,4,5,6,7,10,12,13,15,17,35,44,70,32,67,43]

val=reduce(find_max ,l)
print(val)