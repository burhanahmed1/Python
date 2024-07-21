'''
Write a program to print the following star pattern.
   *
  * *
 *   *
*     *
 *   *
  * *
   *

'''

n=int(input("Enter the number : "))
for i in range(1,n+1):
    print(" "* (n-i),end="")
    if(i==1):
        print("*")
    else:
        print("*",end="")
        print(" "* ((2*i)-3),end="")
        print("*")

for i in range(n-1,0,-1):
    print(" "* (n-i),end="")
    if(i==1):
        print("*",end="")
    else:
        print("*",end="")
        print(" "* ((2*i)-3),end="")
        print("*")

