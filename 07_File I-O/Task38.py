# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’

with open("Poems.txt","r") as f:
    text=f.read()

for word in text.split(" "):
    if(word =="Twinkle"):
        print("Found")


