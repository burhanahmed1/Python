# Write a program to find out whether a file is identical & matches the content of  another file.

with open("Python.txt","r") as f:
    content=f.read()

with open("Python_copy.txt","r") as g:
    content1=g.read()

if content==content1:
    print("Both files are identical")
else:
    print("Both files are different")