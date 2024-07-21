# Write a program to find out whether a given post is talking about “Harry” or not.

post=str(input("Write your post here : "))
person=str(input("Enter the person name to find in post : "))

if (person in post):
    print(f"This post is talking about {person}")
else:
    print(f"This post is not talking about {person}")