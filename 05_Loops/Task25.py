# Write a program to print the following star pattern.
#   *
#  ***
# *****

num=int(input("Enter the number : "))
for i in range(1, num+1):
    print(" "* (num-i),end="")
    print("*"* (2*i-1),end="")
    print("")