# Write a python function to remove a given word from a list ad strip it at the same time.

def remove_item(l,r):
    n=[]
    for item in l:
        if (item != r) :
            n.append(item.strip(r))
    return n




list=[]
s=int(input("Enter the size of list : "))
for i in range(1,s+1):
    n=input(f"Enter {i} item in the list : ")
    list.append(n)

r=input("Enter the item you want to remove from list : ")
new_list=remove_item(list,r)
print(new_list)