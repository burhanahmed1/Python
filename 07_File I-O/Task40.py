'''
Write a program to generate multiplication tables from 2 to 20 and write it to the 
different files. Place these files in a folder for a 13 – year old.
'''

def print_tables(first,last):
    if(first<1):
        first=2
    if(last<1):
        last=2

    for i in range(first,last+1):
        with open(f"Tables/Table{i}.txt","w") as f:
            for j in range(1,11):
                f.writelines(f"{i} x {j} = {i*j}\n")

print_tables(2,20)