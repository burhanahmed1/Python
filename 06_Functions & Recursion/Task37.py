# Write a python function to print multiplication table of a given number

def print_table(n,i):
    if(i!=0):
        print_table(n,i-1)
        print(f"{n} x {i} = {n*i}")
    return 

n=int(input("Enter the number : "))
print_table(n,10)
