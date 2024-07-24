a=int(input("Enter the value of a : "))

try:
    b=int(input("Enter the value of b : "))
except ZeroDivisionError as z:
    print("Infinite")

else:
    print(f"{a}/{b} = {a/b}")

