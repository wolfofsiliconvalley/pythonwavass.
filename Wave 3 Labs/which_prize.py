points = 174

if points <= 50:
    i = "wooden rabbit!"
elif 51 <= points <= 150:
    i = "no prize"
elif 151 <= points <= 180:
    i = "wafer-thin mint!"
elif 181 <= points <= 200:
    i = "penguin"
else:
    i = "O.Y.O"
result = f"Congratulations! You won a a {i}"

print(result)