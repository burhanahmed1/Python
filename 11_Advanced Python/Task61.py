'''
Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not 
present, a message without exiting the program must be printed prompting the same.
'''

try:
    with open("1.txt","r") as f1:
        f1.read()
except Exception as e:
    print(e)

try:
    with open("2.txt","r") as f2:
        f2.read()
except Exception as e:
    print(e)
     
try:
    with open("3.txt","r") as f3:
        f3.read()

except Exception as e:
    print(e)