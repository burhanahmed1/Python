# Write a program to print multiplication table of a given number using for loop.
num=int(input("Enter number to print it's table : "))
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")