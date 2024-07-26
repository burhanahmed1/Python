# Write a program to filter a list of numbers which are divisible by 5.

l=[1,2,3,4,5,6,7,10,12,13,15,17,35,44,70]

f=filter(lambda l:l%5==0,l)
print(list(f))
