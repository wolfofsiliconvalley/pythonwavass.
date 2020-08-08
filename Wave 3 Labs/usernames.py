
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

for name in names:
    newName = name.replace(" ", "_").lower()
    usernames.append(newName)


print(usernames)