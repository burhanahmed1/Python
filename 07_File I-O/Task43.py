# Write a program to mine a log file and find out whether it contains ‘python’.

with open("Python.txt") as f:
    content=f.read()

if("python" in content):
    print("Python is present in the file")
else:
    print("Python not present")