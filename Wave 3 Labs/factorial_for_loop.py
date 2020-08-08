
# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# current number being multiplied
current = 1

# write your for loop here
while (current <= number):
    #multiplying the product by the current number
    product *= current
    
    # increment current with each iteration until it reaches number
    current +=1
    
    print(product)


# print the factorial of number
print(product)