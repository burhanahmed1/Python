# Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
info={}

for i in range(4):
    name=input("Enter name : ")
    lang=input("Enter your language : ")
    info.update({name:lang})

print(info.items())
