# Write a program to fill in a letter template given below with name and date.


letter = '''Dear <|Name|>,
You are selected!
<|Date|>
'''

name=input("Enter your name : ")
print(letter.replace("<|Name|>",name).replace("<|Date|>","2 July,2024"))