# Write a recursive function to calculate the sum of first n natural numbers.

def sum_nums(n):
    if n!=0:
        return sum_nums(n-1)+n
    else :
        return 0
  
n=int(input("Enter the number to calculate sum : "))
print(f"The sum of first {n} natural numbers is {sum_nums(n)}")



