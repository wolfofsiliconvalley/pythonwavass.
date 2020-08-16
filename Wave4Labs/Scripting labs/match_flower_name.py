# match_flower_name
# Method 1
def flower(filename):
    message = input("Enter your First [space] Last name only: ")
    x = []
    with open(filename) as f:
        for name in f:
            if name[0] == message[0]:
                x.append(name)
    return x

x = flower('flowers.txt')
for names in x:
    print(names)

# Method 2
def flower(filename):
    message = input("Enter your First [space] Last name only: ")
    x = []
    with open(filename) as f:
        for name in f:
            if name[0] == message[0]:
                x.append(name)
    return x

print(flower('flowers.txt'))

# Method 3
def flower(filename):
    message = "Bill Newman"
    x = []
    with open(filename) as f:
        for name in f:
            if name[0] == message[0]:
                x.append(name)
    return x


x = flower('flowers.txt')
for names in x:
    print(names)