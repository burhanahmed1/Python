# Repeat program 4 for a list of such words to be censored.

words=["Donkey","animal","fool"]

with open("Donkey.txt","r") as f:
    content=f.read()

for word in words:
    content=content.replace(word,"#####")

with open("Donkey.txt","w") as f:
    f.write(content)