'''Write a program to print the following star pattern.
   *
  * *
 *   *
*******
'''

n=int(input("Enter the number : "))
for i in range(1,n+1):
    print(" "* (n-i),end="")
    if(i==1):
        print("*",end="")
    elif(i==n):
        print("*"* ((2*n)-1),end="")
    else:
        print("*",end="")
        print(" "* ((2*i)-3),end="")
        print("*",end="")

    print("")


