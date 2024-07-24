# Store the multiplication tables generated in problem 3 in a file named Tables.txt.

n=int(input("Enter the number to print table."))
l2= [f"{n} x {i} = {n*i}" for i in range(1,11)]

with open("Tables.txt","w") as f:
    f.write(f"{l2}\n")
