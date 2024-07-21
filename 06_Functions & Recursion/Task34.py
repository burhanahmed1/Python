'''
Write a python function to print first n lines of the following pattern:
***
** 
*
'''

def inverse_triangle(n):
    if(n!=0):
        print("*"* n)
        inverse_triangle(n-1)
    return

n=int(input(("Enter the number : ")))
inverse_triangle(n)