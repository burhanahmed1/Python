#Write a program to accept marks of 6 students and display them in a sorted

Marks = []
for i in range(6):
    Mark=input(f"Enter marks for student {i+1}: ")
    Marks.append(Mark)

Marks.sort()
print(Marks)