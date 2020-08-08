usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
for item in range(len(usernames)):
    usernames[item] = usernames[item].lower().replace(" ", "_")

print(usernames)