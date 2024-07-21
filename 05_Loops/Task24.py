# Write a program to calculate the factorial of a given number using for loop.
num=int(input("Enter a number : "))
fac=1
for i in range(num):
    fac*=(i+1)

print(f"Factorial of {num} is : {fac}")