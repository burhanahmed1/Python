#A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program  to detect these spams.

a = []

for i in range(4) :
    
    h=int(input(f"Enter {i+1} number "))
    a.append(h)

g=0

if a[0]>a[1] and a[0]>a[2] and a[0]>a[3]: 
    g=a[0]
elif a[1]>a[0] and a[1]>a[2] and a[0]>a[3]:
    g=a[1]
elif a[2]>a[0] and a[2]>a[1] and a[2]>a[3]:
    g=a[2]
else:
    g=a[3]

print(f"{g} is greatest")