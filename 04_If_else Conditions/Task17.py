# Write a program which finds out whether a given name is present in a list or not.

names=[]
for i in range(5) :
    n=str(input(f"Enter the name {i+1} in list : "))
    names.append(n)

name=str(input("Enter the name you want to search in the list : "))

if name in names :
    print("Found")
else:
    print("Not Found")