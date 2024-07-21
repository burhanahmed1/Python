#  Write a python program to rename a file to “renamed_by_ python.txt.

with open("Python_copy.txt","r") as f:
    content=f.read()

with open("Renamed_python.txt","w") as f:
    f.write(content)