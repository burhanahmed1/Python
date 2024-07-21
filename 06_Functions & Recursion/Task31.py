#Write a program using functions to find greatest of three numbers.


def max_num(list,n):
    h=0
    for i in range(1,n):
        if (list[i-1]>list[i]):
            h=list[i-1]
        else:
            h=list[i]
    return h

n=int(input("Enter the length of list : "))
l=[]
for i in range(n):
    a=int(input("Enter number : "))
    l.append(a)

b=max_num(l,n)
print(f"The maximum number among {n} numbers is : {b}")