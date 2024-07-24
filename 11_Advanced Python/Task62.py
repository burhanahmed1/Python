# . Write a program to print third, fifth and seventh element from a list using enumerate function.

l=["a","b","c","d","e","f","g","h"]

for i,item in enumerate(l):
    if((i+1)==3 or (i+1)==5 or (i+1)==7):
        print(f"The {i} item of list is {item}.")
